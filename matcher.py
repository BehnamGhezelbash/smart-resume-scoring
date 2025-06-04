# matcher.py
"""
Resume Matcher Module for Mini ATS System
Calculates similarity score between job description and resumes using TF-IDF and cosine similarity.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def calculate_similarity_scores(job_description, resumes):
    """
    Computes cosine similarity scores between a job description and multiple resumes.

    Args:
        job_description (str): Text of the job description.
        resumes (dict): Dictionary of {filename: resume_text}.

    Returns:
        list of tuples: Each tuple contains (filename, score), sorted by score descending.
    """
    results = []
    for filename, resume_text in resumes.items():
        texts = [job_description, resume_text]
        tfidf = TfidfVectorizer(stop_words='english').fit_transform(texts)
        score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        results.append((filename, round(float(score), 4)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results
