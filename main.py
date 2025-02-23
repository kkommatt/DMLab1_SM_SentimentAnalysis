from fetch_tweets import fetch_tweets
from preprocess import preprocess_tweets
from sentiment_analysis import analyze_sentiment
from visualization import plot_sentiment_distribution, generate_wordcloud


def main():
    # For getting tweets using X API (max 100 per month free)

    # print("Fetching tweets...")
    # fetch_tweets()

    print("Preprocessing tweets...")
    preprocess_tweets("data/data.csv")

    print("Performing sentiment analysis...")
    analyze_sentiment()

    print("Visualizing results...")
    plot_sentiment_distribution()
    generate_wordcloud("Positive")


if __name__ == "__main__":
    main()
