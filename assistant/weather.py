import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch current weather for a given city.
    Returns a string that can be spoken by the assistant.
    """

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            weather = data["weather"][0]["description"].title()

            return (
                f"The current weather in {city_name}, {country} is {weather}. "
                f"The temperature is {temperature} degrees Celsius, "
                f"feels like {feels_like} degrees, "
                f"and the humidity is {humidity} percent."
            )

        elif response.status_code == 404:
            return f"Sorry, I couldn't find the city {city}."

        else:
            return "Sorry, I couldn't fetch the weather information right now."

    except requests.exceptions.Timeout:
        return "The weather service is taking too long to respond."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to the weather service."

    except Exception as e:
        print(f"Weather Error: {e}")
        return "An unexpected error occurred while fetching the weather."