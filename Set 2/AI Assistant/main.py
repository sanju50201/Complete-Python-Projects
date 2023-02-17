import datetime
import random
import webbrowser
import requests


# create a class for the Assistant

class Assistant:
    def __init__(self):
        self.responses = [
            "I'm sorry, I don't understand.",
            "I'm sorry, I don't know the answer to that.",
            "Could you please rephrase your question?",
            "I'm not sure I understand.",
            "Let me look that up for you.",
            "I'm sorry i'm not programmed to do that yet.",
            "I'm here to help you, how can I help you?",
            "Sure, I can help you with that.",
            "No problem, I've got you covered.",
            "I'd be happy to help with that.",

        ]

    # method to generate respones
    def generate_response(self, user_input):
        if "time" in user_input:
            now = datetime.datetime.now()
            return "The time currently " + now.strftime("%H:%M:%S")
        elif "weather" in user_input:
            api_key = "77fa53376c096885f3903cf2c8f7bc41"
            url = "http://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid=" + \
                api_key + "&units=imperial"
            response = requests.get(url)
            data = response.json()
            temperature = str(data["main"]["temp"]) + " degrees Fahrenheit"
            description = data["weather"][0]["description"]
            return "The current weather in Bengaluru is " + temperature + " and " + description
        elif "task" in user_input:
            # TODO
            return "Sure, I've added that task for you."
        elif "search" in user_input:
            # Extract the search from the user input
            search_term = user_input[user_input("search") + 7:]
            url = "https://www.google.com/search?q="+search_term
            webbrowser.open(url)
            return "Here is what I found for " + search_term + " on Google."
        else:
            return random.choice(self.responses)

    # method to start the assistant

    def start(self):
        while True:
            user_input = input("How can I assisst you today? ")
            if user_input.lower() == "quit":
                print("Hope i was helpful to you today, Goodbye!")
                break
            response = self.generate_response(user_input)
            print(response)


# create an object to that class

assistant = Assistant()
assistant.start()
