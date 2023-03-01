import requests

# function to get the weather data


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
        return
    else:
        print(f"Current weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°F")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")


def main():
    api_key = "77fa53376c096885f3903cf2c8f7bc41"
    city = input("Enter city: ")
    get_weather(city, api_key)


if __name__ == '__main__':
    main()
