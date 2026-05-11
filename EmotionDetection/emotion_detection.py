import requests
import json

def emotion_detector(text_to_analyze):
    # The URL for the Watson NLP Emotion Analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers for the API request
    header = {"header_id": "emotion_detector_id"}
    
    # The payload/data being sent to the service
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Task 7 logic: Handling blank input (Status Code 400)
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion values
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Finding the emotion with the highest score (Dominant Emotion)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Adding the dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
  
