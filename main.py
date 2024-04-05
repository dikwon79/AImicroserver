# import whisper

# model = whisper.load_model("base")

# model.device

# import whisper
# from IPython.display import Audio
# Audio("test.mp3")

# audio = whisper.load_audio("test22.m4a")
# audio = whisper.pad_or_trim(audio)

# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# print(result.text)
import whisper
import gradio as gr

# Load model
model = whisper.load_model("base")

def transcribe(audio):
   
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

gr.Interface(
    title='O2 ai test',
    fn=transcribe,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath")
    ],
    outputs=[
        "textbox"
    ],
    live=True
).launch()