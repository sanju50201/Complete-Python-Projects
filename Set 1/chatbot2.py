import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors

# Load a pre-trained word2vec model
model = KeyedVectors.load_word2vec_format('path/to/model.bin', binary=True)

# Define a list of predefined responses
responses = [
    "My name is Sanju.",
    "I'm doing well, thank you!",
    "I can answer your questions and engage in conversation.",
    "I'm sorry, I don't understand what you're asking."
]

# Convert the responses to their vector representation
responses_vectors = [model[response.split()] for response in responses]

# Function to get the response for a given input
def get_response(input_text):
    input_words = input_text.split()
    input_vector = np.mean([model[word] for word in input_words if word in model], axis=0)
    similarity = [cosine_similarity([input_vector], [response_vector]) for response_vector in response_vectors]
    most_similar_response_index = np.argmax(similarity)
    return responses[most_similar_response_index]

# Main loop to get input from the user and print the chatbot's response
while True:
    input_text = input("You: ")
    if input_text.lower() == "exit":
        break
    response = get_response(input_text)
    print("Sanju: " + response)
