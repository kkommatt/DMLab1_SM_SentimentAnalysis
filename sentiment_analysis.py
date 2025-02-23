import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    text = str(text)
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def analyze_sentiment(path="data/processed_tweets.csv"):
    df = pd.read_csv(path)
    df["sentiment"] = df["cleaned_tweet"].apply(get_sentiment)
    df.to_csv(path, index=False)
    print("Sentiment analysis complete.")

if __name__ == "__main__":
    analyze_sentiment()
