from textblob import TextBlob

# Sample text

text = input("Enter your text: ")

# performing the sentiment analysis

blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity

# classify sentiment

if sentiment_score > 0:
    sentiment = "positive"
elif sentiment_score < 0:
    sentiment = "negative"
else:
    sentiment = "neutral"


print(f"The sentiment of the '{text}' is: {sentiment}")
