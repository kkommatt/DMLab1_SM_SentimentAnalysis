### **Twitter Sentiment Analysis**
**Analyze sentiments of tweets using NLP and visualization techniques.**  

![Twitter Sentiment Analysis](https://img.shields.io/badge/Twitter%20Sentiment%20Analysis-Python%20%7C%20NLTK%20%7C%20Tweepy-blue)  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---

## **📖 Table of Contents**
- [🔍 Project Overview](#-project-overview)
- [🎯 Features](#-features)
- [🛠️ Technologies Used](#%EF%B8%8F-technologies-used)
- [📂 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [⚙️ Usage](#%EF%B8%8F-usage)
- [📊 Results & Visualizations](#-results--visualizations)
- [📝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙋‍♂️ Contact](#%EF%B8%8F-contact)

---

## 🔍 **Project Overview**
This project fetches recent tweets using **Tweepy**, cleans and preprocesses them using **NLTK**, and performs **sentiment analysis** using **TextBlob**. The results are visualized using **Seaborn and Matplotlib**.

✅ **Objectives:**  
- Extract real-time tweets from Twitter API.  
- Preprocess tweets by removing noise, stopwords, and lemmatizing words.  
- Perform sentiment analysis (Positive, Negative, Neutral).  
- Visualize results with **bar charts** and **word clouds**.  

---

## 🎯 **Features**
✔ Fetches **real-time tweets** using Twitter API.  
✔ Cleans text by removing **URLs, mentions, hashtags, and special characters**.  
✔ Performs **tokenization, stopword removal, and lemmatization**.  
✔ Classifies sentiment as **Positive, Negative, or Neutral**.  
✔ Generates **bar plots and word clouds** for better insights.  

---

## 🛠️ **Technologies Used**
| **Category**  | **Technology** |
|--------------|-----------------|
| **Programming Language** | Python 3.9+ |
| **Twitter API** | Tweepy |
| **NLP Tools** | NLTK, TextBlob |
| **Data Processing** | Pandas |
| **Visualization** | Matplotlib, Seaborn, WordCloud |
| **Environment Management** | dotenv |

---

## 📂 **Project Structure**
```
DMLab1_SM_SentimentAnalysis/
│── .env                    # Environment variables (API keys)
│── requirements.txt        # Required Python packages
│── README.md               # Project documentation
│── main.py                 # Main execution script
│── config.py               # Configuration settings
│── fetch_tweets.py         # Twitter API fetching logic
│── preprocess.py           # Text cleaning and preprocessing
│── sentiment_analysis.py   # Sentiment classification logic
│── visualization.py        # Charts and word cloud generation
│── data/
│   ├── tweets.csv          # Raw tweets dataset
│   ├── processed_tweets.csv # Cleaned and analyzed tweets
│── nltk_data/              # NLTK corpora (stopwords, wordnet, punkt)
```

---

## 🚀 **Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis
```

### **2️⃣ Set Up Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Twitter API**
- Create a **Twitter Developer Account**.
- Generate **Bearer Token** from the Twitter Developer portal.
- Create a `.env` file in the root directory and add:
  ```
  BEARER_TOKEN=your_twitter_bearer_token
  ```

---

## ⚙️ **Usage**
### **Run the entire pipeline**
```sh
python main.py
```
This script will:
1. **Fetch recent tweets** from Twitter API.
2. **Clean and preprocess** tweets.
3. **Analyze sentiment** of tweets.
4. **Visualize results** with graphs and word clouds.

### **Run Individual Modules**
#### Fetch tweets:
```sh
python fetch_tweets.py
```
#### Preprocess tweets:
```sh
python preprocess.py
```
#### Perform sentiment analysis:
```sh
python sentiment_analysis.py
```
#### Visualize results:
```sh
python visualization.py
```

---

## 📊 **Results & Visualizations**
### **1️⃣ Sentiment Distribution**
Generates a bar chart showing the distribution of **Positive, Negative, and Neutral** tweets.  

🔹 **Example Output:**  
![Sentiment Distribution](https://github.com/kkommatt/DMLab1_SM_SentimentAnalysis/blob/master/images/distribution.png)

---

### **2️⃣ Word Cloud of Positive Tweets**
Highlights the most frequently used words in **positive tweets**.  

🔹 **Example Output:**  
![Positive Word Cloud](https://github.com/kkommatt/DMLab1_SM_SentimentAnalysis/blob/master/images/wordcloud.png)

---

## 📝 **Contributing**
Want to improve this project? Follow these steps:  

1. **Fork** the repository.
2. **Create a new branch**:  
   ```sh
   git checkout -b feature-branch
   ```
3. **Make changes and commit**:  
   ```sh
   git commit -m "Added a new feature"
   ```
4. **Push to the branch**:  
   ```sh
   git push origin feature-branch
   ```
5. **Submit a Pull Request**!

---

## 📜 **License**
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🚀 **Future Enhancements**
- 🔹 Use **BERT/LSTM** for sentiment analysis instead of TextBlob.  
- 🔹 Store analyzed tweets in **SQLite/PostgreSQL**.  
- 🔹 Deploy as a **Flask API** with a frontend dashboard.  

---

## ⭐ **Show Some Love**
If you like this project, consider giving it a **🌟 Star** on GitHub! 😊  
