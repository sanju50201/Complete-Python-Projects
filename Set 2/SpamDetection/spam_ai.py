from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


#  create a spam detector class

class SpamDetector:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = CountVectorizer()

    def is_spam(self, message):
        if ',' in message:
            label, text = message.strip().split(',')
            label = int(label)
        else:
            text = message
            label = None
        text = self.process_message(text)
        text_vector = self.vectorizer.transform([text])
        prediction = self.classifier.predict(text_vector)[0]
        if label is not None:
            return prediction, label
        else:
            return prediction

    def process_message(self, message):
        message = message.lower()
        words = word_tokenize(message)
        filtered_words = [
            word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)


# examples
my_message = SpamDetector()
my_message = input("Enter your message: ")
print(my_message.is_spam())
