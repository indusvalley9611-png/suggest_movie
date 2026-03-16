# 🎬 Movie Recommendation System using TF-IDF & Cosine Similarity

## 📌 Project Overview

This project is a **Content-Based Movie Recommendation System** built using Python and Machine Learning techniques.
It recommends similar movies based on **overview text + genres** using **TF-IDF Vectorization** and **Cosine Similarity**.

The goal of this project was to understand how real recommendation systems work (like Netflix / Amazon) using **Natural Language Processing (NLP)** and **Vector Space Models**.

---

## 🚀 Features

* Content-based recommendation
* Uses movie overview + genres
* TF-IDF text vectorization
* Cosine similarity matching
* Multiple movie input support
* Handles missing data
* Genre extraction using AST parsing

---

## 🧠 What I Learned

* TF-IDF Vectorization
* Tokenization
* Stop-word removal
* Lemmatization (concept understanding)
* Text preprocessing
* Cosine similarity
* Feature engineering
* Content-based filtering
* Handling large datasets using Pandas
* Parsing JSON-like text using AST
* Building recommendation systems
* NLP basics in Machine Learning

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* AST (Abstract Syntax Tree)
* NLP concepts

---

## 📂 Dataset Used

movies_metadata.csv
Dataset contains:

* title
* overview
* genres

---

## ▶️ How it Works

1. Load dataset
2. Clean missing values
3. Extract genres from JSON format
4. Combine overview + genres
5. Convert text → TF-IDF vectors
6. Compute cosine similarity
7. Recommend top similar movies

---

## 📸 Example Output

Input Movie: Batman
Recommended:

* The Dark Knight
* Batman Begins
* Superman
* Joker

---

## 📌 Future Improvements

* Add lemmatization using NLTK / spaCy
* Use CountVectorizer / Word2Vec / BERT
* Add GUI / Web app
* Add collaborative filtering
* Deploy using Streamlit

---

## 🔗 Author

Made by: Your Name
B.Tech CSE Student | Machine Learning Learner | Python Developer
