import pyaudio
import wave
import time
import math
import os

CHUNK = 1024  # Number of frames in a buffer
FORMAT = pyaudio.paInt16  # Audio format (16 bits per sample)
CHANNELS = 1  # Number of audio channels (mono)
RATE = 8000  # Sampling rate (Hz)
THRESHOLD = 5000  # Threshold for detect 43535ing silence (in RMS)
SILENCE_LIMIT = 1  # Time limit for detecting silence (in seconds)

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
                    
def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    print(max(snd_data) < THRESHOLD)
    return max(snd_data) < THRESHOLD

def record_audio():
    "Records audio from the microphone and saves it to disk"
    # Start recording

    frames = []
    silent_frames = 0
    started = False
    print("Recording...")
    while True:
        # Read a buffer of audio data from the stream
        data = stream.read(CHUNK)
        # Convert the buffer to a list of samples
        snd_data = list(map(int, data))
        # If the audio is above the 'silent' threshold
        if not is_silent(snd_data):
            # Record the audio
            frames.append(data)
            silent_frames = 0
            started = True
        else:
            # If the audio is below the 'silent' threshold
            silent_frames += 1
            # If we've been below the 'silent' threshold for more than the time limit
            if started and silent_frames > SILENCE_LIMIT * RATE / CHUNK:
                break
    # Stop recording
    print("Recording stopped.")
    # Save the audio to disk
    filename = "recording.wav"
    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
    print("Saved to", filename)

record_audio()
