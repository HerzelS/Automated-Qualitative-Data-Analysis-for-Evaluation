import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    """
    Clean the input text by removing special characters, numbers, and stopwords.
    Args:
        text (str): The input text to be cleaned.
    Returns:
        str: The cleaned text.
    """
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove stopwords
    tokens = [word for word in text.split() if word not in STOPWORDS]
    print(text)
    return " ".join(tokens)

def preprocess_texts(texts: list) -> list:
    """
    Preprocess a list of texts by cleaning each text.
    Args:
        texts (list): A list of strings to be preprocessed.
    Returns:
        list: A list of cleaned strings.
    """
    return [clean_text(t) for t in texts if isinstance(t, str)]