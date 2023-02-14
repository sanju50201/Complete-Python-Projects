import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# load the dataset

data = pd.read_csv("./train.csv", encoding='ISO-8859-1')

# perform the sentiment analysis on each text

sentiment_scores = []

for text in data['text']:
    blob = TextBlob(str(text))
    sentiment_scores.append(blob.sentiment.polarity)


# classify the sentiment

sentiment_class = []

for score in sentiment_scores:
    if score > 0:
        sentiment_class.append("Negative")
    elif score < 0:
        sentiment_class.append("Positive")
    else:
        sentiment_class.append("Neutral")


# visualize the distributions

fig, ax = plt.subplots()
ax.hist(sentiment_scores, bins=20, color='blue')
ax.set_title("Sentiment Distribution")
ax.set_xlabel("Sentiment Score")
ax.set_ylabel("Number of Texts")
plt.show()

# Output sentiment result

data['sentiment'] - sentiment_class
print(data.head())
