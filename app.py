import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

st.title("Aplicativo AMA")
st.image("translate.png", width=200)
try:
    os.mkdir("temp")
except:
    pass
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
    # Crear un archivo temporal en un directorio temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        tts.save(temp_audio_file.name)
        # Leer el archivo temporal y mostrar el reproductor de audio
        audio_bytes = open(temp_audio_file.name, "rb").read()
        st.markdown("## Tu audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        st.markdown("## Texto en audio:")
        st.write(translated_text)
        # Eliminar el archivo temporal después de mostrar el audio
        os.unlink(temp_audio_file.name)
