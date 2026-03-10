import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=300)
    formatted = json.loads(response.text)
    anger_score = formatted['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted['emotionPredictions'][0]['emotion']['sadness']
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    scores['dominant_emotion'] = sorted_scores[0][0]
    
    return scores
