import json

import openai

from env import OPENAI_KEY
from env import OPENAI_ORG
from functions import configs
from functions import functions
from pprint import pprint

openai.organization = OPENAI_ORG
openai.api_key = OPENAI_KEY

SYSTEM_MESSAGE = "Don't make assumptions about what required values to plug into functions. Ask for clarification if " \
                 "a user request is ambiguous. The user's name is Richard Zhu."


def main():

    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

    while True:

        messages.append({"role": "user", "content": input("> ")})
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            temperature=1,
            messages=messages,
            functions=configs,
            function_call="auto"
        )
        response_message = response["choices"][0]["message"]

        if "function_call" in response_message:
            print("func")
            func_name = response_message["function_call"]["name"]
            kwargs = json.loads(response_message["function_call"]["arguments"])
            func_res = functions[func_name](**kwargs)
            if func_res is not None:
                messages.append({"role": "assistant", "content": func_res})
            else:
                messages.pop()

        else:
            print("non func", response_message["content"])
            messages.append({"role": "assistant", "content": response_message["content"]})


main()
