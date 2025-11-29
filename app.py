import streamlit as st
import pandas as pd
import numpy as np
import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.utils import resample
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# --- 1. NLP Setup and Preprocessing ---

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
# Ensure NLTK resources are available if running for the first time
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
stop_words = set(stopwords.words("english"))


@st.cache_data
def preprocess_text(text):
    """Cleans and prepares text for vectorization and modeling."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)  # Remove punctuation and special characters
    words = text.split()
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)


# --- 2. Data Loading and Model Training (Cached) ---


@st.cache_resource
def load_data_and_train_models(json_file_name="dataset.json"):
    """
    Loads data, expands it using alt_questions, trains the Intent model,
    and creates the search vectors, using the categories as-is.
    """
    try:
        with open(json_file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        st.error(
            f"Error: {json_file_name} not found. Please upload it to the same folder as the script."
        )
        return None, None, None, None

    # 2.1 Data Expansion (No Category Mapping Needed)
    expanded_data = []

    # Expand dataset using alt_questions
    for item in data:
        # *** FIX: Robustly check if the item is a dictionary ***
        if not isinstance(item, dict):
            # This is where the error occurred. Skip unexpected data types.
            st.warning(
                f"Skipping unexpected item in JSON: {item}. Please ensure your JSON is a list of dictionaries."
            )
            continue

        # Use .get() for safer access, in case a key is missing
        category = item.get("category", "UNKNOWN")
        question = item.get("question", "")
        answer = item.get("answer", "")
        alt_questions = item.get("alt_questions", [])

        # 1. Add the primary question
        expanded_data.append(
            {"category": category, "question": question, "answer": answer}
        )

        # 2. Add all alternative questions for better intent training
        # Ensure alt_questions is a list before looping
        if isinstance(alt_questions, list):
            for alt_q in alt_questions:
                if alt_q and isinstance(
                    alt_q, str
                ):  # Safety check for empty or non-string entries
                    expanded_data.append(
                        {"category": category, "question": alt_q, "answer": answer}
                    )

    df = pd.DataFrame(expanded_data)
    df["category"] = df["category"].fillna("UNKNOWN")
    df = df[df["category"] != "UNKNOWN"]
    df["processed_question"] = df["question"].apply(preprocess_text)

    # 2.2 Oversampling for Balanced Training
    min_size = 15
    frames = []
    for label in df["category"].unique():
        block = df[df["category"] == label]
        if len(block) < min_size:
            extra = resample(
                block, replace=True, n_samples=min_size - len(block), random_state=42
            )
            frames.append(extra)
    df = pd.concat([df] + frames, ignore_index=True)

    # 2.3 Train Intent Recognition Model
    X = df["processed_question"]
    y = df["category"]

    intent_pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(max_features=5000)),
            (
                "clf",
                LogisticRegression(
                    solver="liblinear", multi_class="ovr", random_state=42
                ),
            ),
        ]
    )
    intent_pipeline.fit(X, y)

    # 2.4 Create Search Vectors (Crucial for Retrieval)
    vectorizer_search = TfidfVectorizer(max_features=5000, min_df=2, max_df=0.90)
    X_search = vectorizer_search.fit_transform(df["processed_question"])

    return df, intent_pipeline, vectorizer_search, X_search


# --- 3. Chatbot Core Logic ---


# Note: The threshold is set to 0.25 here for better question coverage.
def get_answer(
    query, df, intent_pipeline, vectorizer_search, X_search, threshold=0.25, top_k=3
):
    """Retrieves the best answer based on predicted intent and cosine similarity."""

    processed_query = preprocess_text(query)

    # 1. Intent Recognition
    try:
        pred_intent = intent_pipeline.predict([processed_query])[0]
    except Exception:
        return {"response": "I could not predict a category for that question."}

    # 2. Information Retrieval (IR)
    df_filtered = df[df["category"] == pred_intent].copy()

    if df_filtered.empty:
        return {
            "response": f"Intent '{pred_intent}' recognized, but no answers are currently available in that category."
        }

    # 3. Best Match Selection
    q_vec = vectorizer_search.transform([processed_query])
    filtered_vecs = X_search[df_filtered.index]

    sims = cosine_similarity(q_vec, filtered_vecs).flatten()

    top_idx_sorted = np.argsort(-sims)[:top_k]

    top_matches = df_filtered.iloc[top_idx_sorted].to_dict("records")
    for i, idx in enumerate(top_idx_sorted):
        top_matches[i]["similarity"] = sims[idx]

    # Threshold check
    if top_matches[0]["similarity"] < threshold:
        return {
            "response": (
                f"I'm sorry, I couldn't find a good answer in the **{pred_intent}** category "
                f"(Confidence: {top_matches[0]['similarity']:.2%}). "
                "Please try rephrasing your question or asking about something else."
            )
        }

    return {
        "intent": pred_intent,
        "best_match": top_matches[0],
        "top_matches": top_matches,
    }


# --- 4. Streamlit UI ---


def main():
    st.set_page_config(page_title="AUPP FAQ Chatbot Demo", layout="centered")

    st.title("🤖 AUPP FAQ Chatbot Demo")
    st.caption("Using your defined categories and alt_questions for training.")

    # Load data and models
    df, intent_pipeline, vectorizer_search, X_search = load_data_and_train_models()

    if df is None:
        return  # Stop if data loading failed

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Hello! I am the AUPP FAQ Chatbot. How can I help you today?",
            }
        )

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask a question about AUPP..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        response_data = get_answer(
            prompt, df, intent_pipeline, vectorizer_search, X_search
        )

        # Format the response
        if "response" in response_data:
            assistant_response = response_data["response"]
        else:
            best = response_data["best_match"]

            # Start the formatted message
            formatted_response = (
                f"**Intent Category:** `{response_data['intent']}`\n\n"
                f"**Confidence:** `{best['similarity']:.2%}`\n\n"
                f"### 💡 Answer\n"
                f"{best['answer']}"
            )

            # Add related questions
            related_qs = []
            if (
                response_data.get("top_matches")
                and len(response_data["top_matches"]) > 1
            ):
                for i, m in enumerate(response_data["top_matches"][1:], 1):
                    if m["similarity"] > 0.15:
                        related_qs.append(
                            f" - *{m['question']}* (Conf: {m['similarity']:.1%})"
                        )

            if related_qs:
                formatted_response += "\n\n**📚 Related Questions:**\n" + "\n".join(
                    related_qs
                )

            assistant_response = formatted_response

        # Display assistant message
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_response}
        )


if __name__ == "__main__":
    main()
