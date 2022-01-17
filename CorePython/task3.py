# pip install text-to-speech

from text_to_speech import speak 
# speak("Hello World", "en", save=True, file="Hello-World.mp3")

str1 = input("Any string : ") # input from keyboard
speak(str1, "en", save=True, file="task3.mp3")
