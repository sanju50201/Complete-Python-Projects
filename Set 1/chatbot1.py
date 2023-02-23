# This bot works on rule-based approach

# defining a dictionary of predefined responses

responses = {
    "what is your name?": "My name is Bot.",
    "how are you?": "I'm doing fine, Thank you!",
    "what can you do for me?": "I can answer some questions you ask.",
    "default": "I'm sorry, I don't understand what you're asking."
}

# conver the keys in the dictionary to lowercase
responses = {key.lower(): value for key, value in responses.items()}
# function to get the response for a given input


def get_response(input_text):
    input_text = input_text.lower()
    response = responses.get(input_text, responses["default"])
    return response


# Main loop to get input from the user and print the response

while True:
    input_text = input("Your message: ")
    if input_text.lower() == "exit":
        break
    response = get_response(input_text)
    print("Bot: "+response)
