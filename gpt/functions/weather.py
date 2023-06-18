from ._utils import create_arg
from ._utils import create_config
from env import weather_api
import requests

class WeatherGet:

    config = create_config(
        name="weather_get",
        desc="Gets the weather in a city",
        required=["city"],
        city=create_arg(
            desc="The city that the user would like to find the weather in"
        ),
     )

    @staticmethod
    def run(city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            main_weather = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            return f"Weather in {city}: Mainly {main_weather}, {int(temperature - 273)} degrees Celsius, {humidity}% humidity, {wind_speed} meters per second wind speed"
