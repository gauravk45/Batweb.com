<<<<<<< HEAD
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

duration = 10

recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2)

sd.wait()

write("recording0.wav", freq, recording)

wv.write("recording1.wav", recording, freq, sampwidth=2)
=======
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

duration = 10

recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2)

sd.wait()

write("recording0.wav", freq, recording)

wv.write("recording1.wav", recording, freq, sampwidth=2)
>>>>>>> 54acf9adfb3e62c395c5a5041773b767eb40bcd5
