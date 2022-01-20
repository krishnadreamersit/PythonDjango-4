# Speech to text ?
    # sound to text.

# pip install speechrecognition
# pip install pyaudio
# pip install pyttsx3

import speech_recognition as sr
import pyttsx3

filename = "hello.wav"
r = sr.Recognizer()
hellow=sr.AudioFile(filename)
with hellow as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: " + str(e))