import json
import requests

def get_emotion(dict, p_value):
    ''' Function to extrac the key by value '''
    for key,value in dict.items():
        if value == p_value:
            return key
    return none

def emotion_detector(text_to_analyze):
    ''' Function call Walson libraries to detect the Emotion of a sentence '''
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL,json = input, headers=header)

    print(response.status_code)
    response_json = json.loads(response.text)
    
    if response.status_code == 400:
        emotion = {
                    "anger": None, 
                    "disgust": None, 
                    "fear": None, 
                    "joy": None, 
                    "sadness": None, 
                    "dominant_emotion": None
                }
    
    else:
        emotion = response_json["emotionPredictions"][0]["emotion"]
    
        highest_emotion_value = max(emotion.values())
        dominant_emotion = get_emotion(emotion,highest_emotion_value)
        emotion['dominant_emotion'] = dominant_emotion

    return emotion
