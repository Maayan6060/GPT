import nltk
nltk.download('vader_lexicon')
from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

# יצירת היישום Flask
app = Flask(__name__)

# יצירת מודל VADER
sia = SentimentIntensityAnalyzer()

@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    # קבלת נתוני הקלט (JSON)
    data = request.json
    text = data.get("text", "")

    # ניתוח רגשות באמצעות VADER
    sentiment = sia.polarity_scores(text)

    # החזרת התוצאה
    return jsonify(sentiment)
@app.route("/", methods=["GET"])
def analyze_text():
    # קבלת נתוני הקלט (JSON)
    data = request.json
    text = data.get("text", "")

    # ניתוח רגשות באמצעות VADER
    sentiment = sia.polarity_scores(text)

    # החזרת התוצאה
    return jsonify(sentiment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
