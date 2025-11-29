Project Title
AUPP FAQ Chatbot

Overview
This project builds an FAQ chatbot for AUPP.
The system reads a dataset file, trains a text classifier, and returns answers through a simple chat interface.
The goal is fast and accurate responses to student questions.

Features
Predicts the category of each question.
Searches for the closest match using TF-IDF.
Supports alt questions to improve accuracy.
Runs on Streamlit with a smooth chat UI.
Loads and trains the model when the app starts.

Project Structure
app.py
Runs the Streamlit app.
Loads the dataset.
Cleans the text.
Trains the model.
Handles predictions and chat responses.

aupp_chatbot.ipynb
Notebook for testing ideas and trying new improvements.

dataset.json
Main dataset for training.
Each record includes category, question, answer, and optional alt questions.

README.md
Project details and instructions.

How to Set Up

Install Python 3.

Install all packages from requirements.txt.

Place all project files in one folder.

How to Run the App

Open a terminal.

Move to the project folder.

Enter
streamlit run app.py

The browser will open.

Type your question in the chat box.

How to Update the Dataset
Open dataset.json.
Add new questions, answers, and alt questions.
Use short and clear text.
Keep categories consistent.
Restart the app to refresh the model.

Data Quality Tips
Remove duplicates.
Fix grammar and spelling in each question.
Use simple terms so the model learns cleaner patterns.

Troubleshooting
If the app reports missing NLTK data, run the following commands once inside Python:
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

If the app shows no answers for a category, check the dataset for missing keys.
