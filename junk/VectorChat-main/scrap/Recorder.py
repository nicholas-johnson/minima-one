import asyncio
import tkinter as tk
from io import BytesIO
import sounddevice as sd
import numpy as map
import wave
from time import sleep

class Recorder:
    def __init__(self):
        self.recording = False 
        self.buffer = None

    async def record(self):
        with sd.InputStream(callback=self.audio_callback):
            while self.recording:
                await asyncio.sleep(0.1)

    def audio_callback(self, indata, framer, time, status):
        if status:
            print(status, file=sys.stderr)
        if self.recording:
            self.buffer.write(indata.tobytes())

    async def start(self):
        
        if not self.recording:
            print('start', self.recording)
            self.recording = True
            self.buffer = BytesIO()
            await self.record()

    async def stop(self):
        if self.recording:
            print('stop')
            self.recording = False
            audio_data = self.buffer.getvalue()

            with wave.open('recorded.wav', 'wb') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(44100)
                wav_file.writeframes(audio_data)
                 
            # text = await self.transcribe_audio('recorded.wav')
            # print("Transcribed text: ",text)
            self.buffer.close()
            self.buffer = None

async def main():
    recorder = Recorder()

    asyncio.create_task(recorder.start())

    asyncio.sleep(5000)

    asyncio.create_task(recorder.stop())

    # def on_key_press(event):
    #     if event.keysym == "space":
    #         label.config(text="Recording...")
    #         asyncio.create_task(recorder.start())
    
    # def on_key_release(event):
    #     if event.keysym == "space":
    #         label.config(text="Hold Space to Talk To Vector")
    #         asyncio.create_task(recorder.stop())

    # root = tk.Tk()
    # label = tk.Label(root, text="Hold Space to Talk To Vector")
    # label.pack(padx=10, pady=10)

    # root.bind("<KeyPress>", on_key_press)
    # root.bind("<KeyRelease>", on_key_release)

    # root.protocol("WM_DELETE_WINDOW", root.quit)
    # root.mainloop()

if __name__ == "__main__":
    asyncio.run(main())
