from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic

def run_topic_modeling(texts: list):
    vectorizer = CountVectorizer(stop_words="english")
    topic_model = BERTopic(vectorizer_model=vectorizer)
    topics, probs = topic_model.fit_transfrom(texts)
    return topic_model, topics, probs
     