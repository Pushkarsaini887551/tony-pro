import gradio as gr
from TTS.api import TTS

# मॉडल लोड करें
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

def predict(text, language):
    tts.tts_to_file(text=text, file_path="output.wav", speaker_wav="reference.wav", language=language)
    return "output.wav"

demo = gr.Interface(fn=predict, inputs=["text", "dropdown"], outputs="audio")
demo.launch()
import gradio as gr

# Hugging Face का बेहतरीन प्रीमियम मॉडल इस्तेमाल करें
demo = gr.load("models/facebook/mms-tts-eng")

demo.launch()

