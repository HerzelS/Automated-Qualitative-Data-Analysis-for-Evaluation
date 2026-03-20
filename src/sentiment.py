import nltk
from nltk.sentiment import SentimetIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimetIntensityAnalyzer()

def analyze_sentiment(texts: list) -> list:
    """
    Analyze the sentiment of a list of texts and return the results.
    Args:
        texts (list): A list of strings to be analyzed for sentiment.           
    Returns:
        list: A list of dictionaries containing the sentiment scores for each text. 
    """
    return [sia.polarity_scores(str(t))["compound"] for t in texts]