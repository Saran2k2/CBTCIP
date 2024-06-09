import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def record_audio(duration, sample_rate=44100, filename="output.wav"):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording complete. Saving the file...")
    write(filename, sample_rate, recording)
    print(f"File saved as {filename}")

def play_audio(filename):
    from scipy.io.wavfile import read
    import sounddevice as sd
    
    print(f"Playing {filename}...")
    sample_rate, data = read(filename)
    sd.play(data, sample_rate)
    sd.wait()  # Wait until playback is finished
    print("Playback complete.")

# Example usage:
duration = 5  # seconds
filename = "output.wav"

record_audio(duration, filename=filename)
play_audio(filename)
