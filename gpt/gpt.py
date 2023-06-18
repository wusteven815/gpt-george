import json

import openai

from env import OPENAI_KEY
from env import OPENAI_ORG
from env import USER_NAME
from .functions import configs
from .functions import functions

openai.organization = OPENAI_ORG
openai.api_key = OPENAI_KEY

SYSTEM_MESSAGE = f"Don't make assumptions about what required values to plug into functions. Ask for clarification " \
                 f"if a user request is ambiguous. The user's name is {USER_NAME}."


class GPTHandler:

    def __init__(self):
        self.messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

    def request(self, message):

        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            temperature=1,
            messages=self.messages,
            functions=configs,
            function_call="auto"
        )
        response_message = response["choices"][0]["message"]

        if "function_call" in response_message:
            print("- Function call -")
            func_name = response_message["function_call"]["name"]
            kwargs = json.loads(response_message["function_call"]["arguments"])
            func_res = functions[func_name](**kwargs)
            if func_res is not None:
                self.messages.append({"role": "assistant", "content": func_res})
            else:
                self.messages.pop()

        else:
            print("- Non function call -")
            print(response_message["content"])
            self.messages.append({"role": "assistant", "content": response_message["content"]})
