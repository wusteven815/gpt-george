import json, requests
from api_keys import OPENAI_API_KEY
from emotion_analysis import get_emotion

api_url = "https://api.openai.com/v1/chat/completions"

file = 'Hume\media\IMG_1083.mov'
task = get_emotion(file)
data = json.loads(task)
emotions_text = ", ".join(data["emotions"]).lower()

prompt = data["text"] + " Reply to me as if I am feeling " + emotions_text + "."
print(f"User: {prompt}")

# Example conversation history and user message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the World Series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"},
    {"role": "assistant", "content": "The 2020 World Series was played at Globe Life Field in Arlington, Texas."},
    {"role": "user", "content": "How can I take care of my baby? Reply to me as if I were feeling angry, frustrated, dissapointed."},
    {"role": "assistant", "content": "Parenting is a demanding task, and I understand it may be frustrating at times. You may even be disappointed of how it's turning out. However, it's important to watch your anger, and to approach it with patience and a calm mindset. Seek support from your partner, family, or friends, establish routines for your baby, prioritize self-care, and be open to learning and adapting."},
    {"role": "user", "content": prompt}
]

payload = {
    "messages": conversation,
    "model": "gpt-4"
}

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(api_url, headers=headers, json=payload)
gpt_response = response.json()
result = gpt_response['choices'][0]['message']['content']
print(f"\nChatbot: {result}")
