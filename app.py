from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import json
import string
import os

load_dotenv()

def clean_text(text):
    # lowercase, removes punctuation, and strip whitespace
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

with open('phrase_map.json', 'r') as f:
    phrase_map = json.load(f)

speech_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SERVICE_REGION")

app = Flask(__name__)

def recognize_speech():
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Listening...")
    result = recognizer.recognize_once()
    print("Recognition complete")

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        recognized = result.text.strip().lower()
        print(f"Recognized: {recognized}")
        return recognized
    else:
        return None

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/listen', methods=['GET'])
def listen_and_match():
    recognized_text = recognize_speech()
    if not recognized_text:
        return jsonify({
            "status": "error",
            "recognized_text": "(could not recognize speech)"
        }), 200

    cleaned_input = clean_text(recognized_text)

    matched_key = None
    matched_phrase = None
    for phrase in phrase_map:
        cleaned_phrase = clean_text(phrase)
        if cleaned_phrase in cleaned_input:
            matched_key = phrase_map[phrase]
            matched_phrase = phrase
            break

    return jsonify({
        "status": "success",
        "recognized_text": recognized_text,
        "matched_phrase": matched_phrase,
        "sign_id": matched_key
    })

if __name__=='__main__':
    app.run(debug=True)