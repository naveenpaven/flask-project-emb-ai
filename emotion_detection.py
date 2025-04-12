import json
import requests

def get_emotion(dict, p_value):
    for key,value in dict.items():
        if value == p_value:
            return key
    return none

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL,json = input, headers=header)

    response_json = json.loads(response.text)
    emotion = response_json["emotionPredictions"][0]["emotion"]
    
    highest_emotion_value = max(emotion.values())
    dominant_emotion = get_emotion(emotion,highest_emotion_value)
    emotion['dominant_emotion'] = dominant_emotion

    return emotion
