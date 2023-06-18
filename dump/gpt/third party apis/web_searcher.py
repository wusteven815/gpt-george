from googlesearch import search
import requests
from api_keys import news_api, weather_api

NEWS_API=news_api
WEATHER_API=weather_api

def google_search(keyword):
    query = keyword
    list_response = []
    for j in search(query, num=5, stop=10, pause=2):
        list_response += j
    return list_response




def get_latest_news(api_key, keyword):
    if keyword == 'null':
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data['articles']
        list_response = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            list_response.append((title, source))
    else:
        print("Error fetching news. Please try again later.")
    return data


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Main: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        return {
            'main': main_weather,
            'description': description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    else:
        print("Error fetching weather. Please try again later.")



get_weather('berkeley' ,WEATHER_API)