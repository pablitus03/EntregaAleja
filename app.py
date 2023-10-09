import streamlit as st
from googletrans import Translator
from gtts import gTTS

st.title("Aplicativo AMA")
st.image("translate.png", width=200)
st.subheader("Texto a audio y traducción.")
text = st.text_input("Ingrese el texto:")
languages = {"Inglés": "en", "Español": "es", "Chino Mandarín": "zh-cn", "Francés": "fr", "Ruso": "ru", "Hindi": "hi"}
target_lang = st.selectbox("Seleccione el idioma de destino:", list(languages.keys()))
if text and target_lang:
    source_lang = "es"
    target_lang_code = languages[target_lang]
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang_code).text
    tts = gTTS(translated_text, lang=target_lang_code, slow=False)
    tts.save("temp/audio.mp3")
    audio_file = open("temp/audio.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown("## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    st.markdown("## Texto en audio:")
    st.write(translated_text)
