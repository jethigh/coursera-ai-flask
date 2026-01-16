"""This module makes emotion analisis of provided text"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flas application
app = Flask("Emotion Detector")

# Create emotionDetector endpoint using decorator
@app.route("/emotionDetector")
def send_to_emotion_detector():
    '''
    This function sends provided text to emotion detector
    '''
    # Get tex to analyze from JavaScript
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze text
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    # Return formatted output
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Render index.html
@app.route("/")
def render_index_page():
    '''
    This function render index.html on / endpont
    '''
    return render_template('index.html')

# Start development server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
