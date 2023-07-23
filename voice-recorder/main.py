import sounddevice
from scipy.io.wavfile import write

# Sample rate
fs = 44100

# Ask to enter the recording time
second = int(input("Recording time in second: "))
print("Recording... \n")

record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)
sounddevice.wait()
write("My Recording.wav", fs, record_voice)

print("Recording is done. Check your directory to listen recording.")