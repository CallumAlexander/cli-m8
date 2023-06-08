import requests


def fetch_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


def display_weather(data):
    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")


def main():
    api_key = input("Enter API key for OpenWeatherMap >  ")
    city = input("Enter a city name > ")

    weather_data = fetch_weather(api_key, city)

    if weather_data["cod"] == 200:
        display_weather(weather_data)
    else:
        print(f"Error fetching weather data. Please try again.\n{weather_data['message']}")


if __name__ == "__main__":
    main()