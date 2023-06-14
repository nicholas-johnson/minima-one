import openai
import threading

OPENAI_API_KEY = "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"

class WhisperASR:
    def __init__(self, on_transcription_complete):
        self.api_key = OPENAI_API_KEY
        if self.api_key is None:
            raise Exception("OPENAI_API_KEY not found in environment variables.")
        openai.api_key = self.api_key
        self.on_transcription_complete = on_transcription_complete

    def _transcribe(self, file_path): 
        audio_file= open(file_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        self.on_transcription_complete(transcript['text'])
        return transcript

    def transcribe(self, file_path):
        thread = threading.Thread(target=self._transcribe, args=(file_path,))
        thread.start()
        
        
if __name__ == "__main__":
    def callback(text):
        print(text)

    transcriber = WhisperASR(callback)
    transcriber.transcribe('output.wav')
