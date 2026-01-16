import requests

def emotion_detector(text_to_analyze):
    # Request config
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_input = { "raw_document": { "text": text_to_analyze } }
    # Make POST request to Watson endpoint
    response = requests.post(url, json = my_input, headers=header)
    # Return text from response object
    return response.text
