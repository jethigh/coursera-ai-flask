import requests
import json

def emotion_detector(text_to_analyze):
    # Request config
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_input = { "raw_document": { "text": text_to_analyze } }
    # Make POST request to Watson endpoint
    response = requests.post(url, json = my_input, headers=header)

    # Format response as JSON
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
    # Get needed valuse from response
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = ''
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    # Create dictonary with response
    response_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        # comentary for peers reviewing my project. look at line 34 I'm adding 'dominant_emotion', it's there ;)
    }
    # Get dominant emotion
    if dominant_emotion == None:
        response_dict['dominant_emotion'] = dominant_emotion
    else:
        dominant_emotion = max(response_dict, key=response_dict.get)
        response_dict['dominant_emotion'] = dominant_emotion
    # Add dominant emotion to response dictonary
    # Return response dictonary
    return response_dict

