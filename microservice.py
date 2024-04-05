from flask import Flask, request
from flask_cors import CORS
import whisper

# Load model
model = whisper.load_model("base")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'audio' not in request.files:
        return 'No audio file provided', 400

    audio_file = request.files['audio']
    audio_file.save('uploaded_audio.wav')
    
    audio_to_txt = transcribe("uploaded_audio.wav")
    print(audio_to_txt)
    return audio_to_txt

def transcribe(audio):
   
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text



if __name__ == '__main__':
    app.run(debug=True)
