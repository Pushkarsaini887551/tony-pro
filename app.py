import streamlit as st
from gtts import gTTS
import os

st.title("Tony Pro - AI Voice Studio")
text = st.text_area("अपनी स्क्रिप्ट यहाँ लिखें:")

if st.button("आवाज़ बनाएं"):
    if text:
        tts = gTTS(text, lang='hi')
        tts.save("output.mp3")
        st.audio("output.mp3")
    else:
        st.warning("कृपया पहले स्क्रिप्ट लिखें!")

