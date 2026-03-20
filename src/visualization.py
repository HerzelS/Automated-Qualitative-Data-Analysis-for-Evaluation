import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def plot_wordcloud(texts: list):
    """"
    Generate and display a word cloud from a list of texts.
    Args:
        texts (list): A list of strings to be used for generating the word cloud.
    """
    all_text = " ".join(texts)
    wc = WordCloud(width=800, height=400, background_color="white").generate(all_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
def plot_sentiment_distribution(sentiments: list):
   
    pd.Series(sentiments).hist(bins=20)
    pd.title("Sentiment Distribution")
    plt.xlabel("Compound Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()