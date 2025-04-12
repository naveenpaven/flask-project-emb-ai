from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    output = ""
    rowcount = 1
    for key,value in response.items():
        if key != "dominant_emotion" and rowcount != len(response) -1:
            output = output + "'" + key + "': " + str(value) + ", "

        if rowcount == len(response) -1:
            output = output + "and '" + key + "': " + str(value) + ". "

        if key == "dominant_emotion":
            output = output + "The dominant emotion is " + value + "."
    
        rowcount += 1

    return f"For the given statement, the system response is  {output}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
