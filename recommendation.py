from stop_words import safe_get_stop_words
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def get_recommended(selected_anime):
    stop_words = safe_get_stop_words('russian')
    data = pd.read_csv('cleaned_anime.csv')
    data.Description = data.Description.fillna(' ')

    tfidf = TfidfVectorizer(stop_words)
    tfidf_matrix = tfidf.fit_transform(data['Description'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(data.index, index=data['Rus_name']).drop_duplicates()
    title = selected_anime.name_rus
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx[0]]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    return data.iloc[movie_indices]
