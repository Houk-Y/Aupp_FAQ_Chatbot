📖 Overview
FAQ chatbot for AUPP

Reads dataset file, trains a text classifier

Returns answers through a simple chat interface

Goal: fast and accurate responses to student questions

✨ Features
Predicts the category of each question

Searches for closest match using TF-IDF

Supports alt questions to improve accuracy

Runs on Streamlit with a smooth chat UI

Loads and trains the model when the app starts

📂 Project Structure
app.py

Runs the Streamlit app

Loads the dataset

Cleans the text

Trains the model

Handles predictions and chat responses

aupp_chatbot.ipynb

Notebook for testing ideas and improvements

dataset.json

Main dataset for training

Each record includes: category, question, answer, alt questions

README.md

Project details and instructions

⚙️ How to Set Up
Install Python 3

Install all packages from requirements.txt

Place all project files in one folder

▶️ How to Run the App
Open a terminal

Move to the project folder

Run:

bash
streamlit run app.py
Browser will open automatically

Type your question in the chat box

📝 How to Update the Dataset
Open dataset.json

Add new questions, answers, and alt questions

Use short and clear text

Keep categories consistent

Restart the app to refresh the model

✅ Data Quality Tips
Remove duplicates

Fix grammar and spelling

Use simple terms so the model learns cleaner patterns

🛠️ Troubleshooting
Missing NLTK data: Run inside Python:

python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
No answers for a category: Check dataset for missing keys (category, question, answer)
