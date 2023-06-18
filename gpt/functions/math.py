from ._utils import create_arg
from ._utils import create_config
import requests
from env import math_api

class MathMode:

    config = create_config(
        name="do_math",
        desc="Answers all math related questions.",
        required=["input"],
        input=create_arg(
            desc="The math related request that the user would like to be answered. If the input is not valid, reprompt the user."
        ),
    )

    @staticmethod
    def run(input):
        input = input.replace(" ", "+")
        print(input)
        url = f"https://www.wolframalpha.com/api/v1/result?input={input}&appid={math_api}&format=plaintext"
        response = requests.get(url)
        return response.text