import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


def plot_sentiment_distribution(path="data/processed_tweets.csv"):
    df = pd.read_csv(path)
    sns.countplot(x=df["sentiment"])
    plt.title("Sentiment Distribution")
    plt.show()


def generate_wordcloud(sentiment="Positive", path="data/processed_tweets.csv"):
    df = pd.read_csv(path)
    text = " ".join(tweet for tweet in df[df["sentiment"] == sentiment]["cleaned_tweet"])

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Most Common Words in {sentiment} Tweets")
    plt.show()


if __name__ == "__main__":
    plot_sentiment_distribution()
    generate_wordcloud("Positive")
