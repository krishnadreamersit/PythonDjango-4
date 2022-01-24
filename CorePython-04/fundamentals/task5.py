# Record sound from user?
# pip install sounddevice
# pip install wavio
# pip install scipy

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100 # Sampling frequency
duration = 5 # Recording duration

# Start recorder with the given values of
# duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()

write("recording1.wav", freq, recording)
wv.write("recording2.wav", recording, freq, sampwidth=2)