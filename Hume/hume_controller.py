import json
from env import OPENAI_KEY
from .emotion_analysis import get_emotion
from gpt import gpt
from audio import audio

api_url = "https://api.openai.com/v1/chat/completions"

file = './input.wav'
def get_result():
    task = get_emotion(file)
    data = json.loads(task)
    emotions_text = ", ".join(data["emotions"]).lower()

    prompt = audio.RESPONSE + " Reply to me as if I am feeling " + emotions_text + "."
    response = gpt.request(prompt)
    gpt_response = response.json()
    result = gpt_response['choices'][0]['message']['content']
    return(f"\nChatbot: {result}")
