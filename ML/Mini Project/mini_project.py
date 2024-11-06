import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("movie_dataset.csv")
df

features = ['keywords', 'cast', 'genres', 'director']
df['keywords'] = df['keywords'].astype(str)
df['cast'] = df['cast'].astype(str)
df['genres'] = df['genres'].astype(str)
df['director'] = df['director'].astype(str)

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]

df['combined_features'] = df.apply(combine_features, axis=1)

df['combined_features'] = df['combined_features'].fillna('')

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(df['combined_features'])

cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]['title'].values[0]

def get_index_from_title(title):
    return df[df.title == title].index.values[0]

movie_index = get_index_from_title('Avatar')

sim_scores = list(enumerate(cosine_sim[movie_index]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
sim_scores = sim_scores[1:11]

for i, score in sim_scores:
    print(get_title_from_index(i))