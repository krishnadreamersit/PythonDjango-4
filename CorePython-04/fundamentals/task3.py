# Text to Speech?
# pip install gTTS pyttsx3 playsound

from gtts import gTTS
import os

str1 = 'Welcome'
language = 'en'
obj1 = gTTS(text=str1, lang=language, slow=False)
obj1.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")

