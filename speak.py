from flask import Flask, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/speak', methods=['GET'])
def speak():
    text = request.args.get('text')
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")
    return "Speaking: " + text

if __name__ == '__main__':
    app.run()
