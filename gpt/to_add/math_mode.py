import requests
from api_keys import math_api

APP_ID = math_api

def get_wolframalpha_response(input):
    url = f"https://www.wolframalpha.com/api/v1/result?input={input}&appid={APP_ID}&format=plaintext"
    response = requests.get(url)

    print(response.text)
    return response.text


get_wolframalpha_response("whats 8 factorial")