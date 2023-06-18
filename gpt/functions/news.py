from ._utils import create_arg
from ._utils import create_config
from env import news_api
import requests

class NewsGet:

    config = create_config(
        name="news_get",
        desc="Gets the latest news for a topic",
        required=["topic"],
        topic=create_arg(
            desc="The topic that the user would like to find the latest news for. If no topic is given, use 'null'"
        ),
     )

    @staticmethod
    def run(topic):
        if topic == 'null':
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
        else:
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api}"
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
        return f"{articles[0]['title']} from {articles[0]['source']['name']}"