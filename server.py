from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flas application
app = Flask("Emotion Detector")

# Create emotionDetector endpoint using decorator
@app.route("/emotionDetector")
def send_to_emotionDetector():
    # Get tex to analyze from JavaScript
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze text
    response = emotion_detector(text_to_analyze)
    # Return formatted output
    return (
        "For the given statement, the system response is 'anger': {}, "
        "'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}."
    ).format(
        response['anger'],
        response['disgust'],
        response['fear'],
        response['joy'],
        response['sadness'],
        response['dominant_emotion']
    )

# Render index.html
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Start development server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)