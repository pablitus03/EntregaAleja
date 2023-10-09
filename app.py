from googletrans import Translator
from gtts import gTTS
import os

frase = input("Ingresa la frase que quieres traducir: ")
idioma_destino = input("Ingresa el idioma de destino (por ejemplo, 'es' para español): ")

traductor = Translator()
traduccion = traductor.translate(frase, dest=idioma_destino)
frase_traducida = traduccion.text

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text
