import tweepy
import pandas as pd
from config import BEARER_TOKEN

def fetch_tweets(query="Python programming -is:retweet lang:en", max_results=100, path="data/tweets.csv"):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["text"])

    if tweets.data:
        data = pd.DataFrame([[tweet.text] for tweet in tweets.data], columns=["tweet"])
        data.to_csv(path, index=False)
        print(f"Fetched {len(data)} tweets.")
    else:
        print("No tweets found.")

if __name__ == "__main__":
    fetch_tweets()
