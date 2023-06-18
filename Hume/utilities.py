import json

def get_emotions(text, data):
    try:
        # text = data[0]['results']['predictions'][0]['models']['prosody']['grouped_predictions'][0]['predictions'][0]['text']
        emotions_list = data[0]['results']['predictions'][0]['models']['prosody']['grouped_predictions'][0]['predictions'][0]['emotions']

        emotions_list = sorted(emotions_list, key=lambda x: x['score'], reverse=True)[:2]

        result_dict = {"text": text, "emotions": {}}
        for emotion in emotions_list:
            result_dict["emotions"][emotion['name']] = emotion['score']
        return json.dumps(result_dict, indent=4)
    except:
        result_dict = {"text": text, "emotions": []}
        return json.dumps(result_dict, indent=4)


