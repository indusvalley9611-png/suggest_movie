import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# ---------------- LOAD ----------------
df = pd.read_csv(
    "movies_metadata.csv",
    low_memory=False,
    usecols=["title", "overview", "genres"]
)
# ---------------- CLEAN ----------------

df["overview"] = df["overview"].fillna("")
df["genres"] = df["genres"].fillna("")
# ---------------- FIX GENRES ----------------

def get_genres(x):
    try:
        g = ast.literal_eval(x)
        return " ".join([i["name"] for i in g])
    except:
        return ""
df["genres"] = df["genres"].apply(get_genres)
# ---------------- FEATURE ----------------

df["text"] = df["overview"] + " " + df["genres"]
# ---------------- TFIDF ----------------
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["text"])

# ---------------- SIMILARITY ----------------
similarity = cosine_similarity(X)

# ---------------- FUNCTION ----------------

def recommend(movie_name):
    movie_name = movie_name.lower()
    titles = df["title"].str.lower()
    if movie_name not in titles.values:
        print("\nMovie not found\n")
        return
    idx = titles[titles == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print("\nInput Movie:", movie_name)
    print("Recommended movies:\n")
    for i in scores[1:5]:
        print(df.iloc[i[0]]["title"])

    print("\n----------------------\n")
# ---------------- MULTIPLE INPUT ----------------

movie1 = input("Enter movie 1: ")
recommend(movie1)

movie2 = input("Enter movie 2: ")
recommend(movie2)

movie3 = input("Enter movie 3: ")
recommend(movie3)
