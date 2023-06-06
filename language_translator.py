import speech_recognition as sr
import googletrans
import pyttsx3
import time

from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translation = None
    retries = 3
    while retries > 0:
        try:
            translation = translator.translate(text, dest=dest_lang)
            break
        except googletrans.exceptions.TranslatorError:
            print("Translation failed. Retrying...")
            retries -= 1
            time.sleep(2)
    return translation.text if translation is not None else ""

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Recognized text:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
        except sr.RequestError as e:
            print("Speech recognition service error: {0}".format(e))

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    dest_lang = 'en'  # Destination language for translation

    # Translate audio
    recognized_text = recognize_speech()
    if recognized_text:
        translated_text = translate_text(recognized_text, dest_lang)
        print("Translated text:", translated_text)
        speak_text("Translated text: " + translated_text)
    else:
        print("No audio input was recognized.")