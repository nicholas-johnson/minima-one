import openai
import threading

OPENAI_API_KEY = "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"

class ChatCompletion:
    def __init__(self, on_complete):
        self.api_key = OPENAI_API_KEY
        self.on_complete = on_complete

    def _complete(self, convo):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=convo)
        answer = completion.choices[0].message.content
        print(answer)
        self.on_complete(answer)
        return answer

    def complete(self, convo):
        thread = threading.Thread(target=self._complete, args=(convo,))
        thread.start()

