import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jobs(skills, csv_path='dataset/jobs.csv'):
    df = pd.read_csv(csv_path)

    # Combine the text columns that describe the job
    df['Combined'] = df['Feature'].astype(str) + " " + df['Category']

    user_skills = ' '.join(skills)
    corpus = df['Combined'].tolist() + [user_skills]

    vectorizer = CountVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()

    cosine_sim = cosine_similarity(vectors)
    scores = cosine_sim[-1][:-1]

    df['Match_Score'] = scores
    df = df.sort_values(by='Match_Score', ascending=False)

    return df[['Category', 'Feature', 'Match_Score']].head(10)
