
import openai
import anki_vector
import tkinter as tk

from action_list import ActionList
from action import Action
# from action_list_watcher import ActionListWatcher
from recorder_window import RecorderWindow
from whisper_asr import WhisperASR 
from chat_completion import ChatCompletion
from conversation import Conversation
from action_factory import ActionFactory
from vector_controller import VectorController
from audio_recorder import AudioRecorder

def create_app():
    def on_transcription_ready(transcript):
        print(transcript)
        conversation.add_message_from_user(transcript)
        # print(conversation.get_convo())

    def on_chat_completion(completion):
        conversation.add_message_from_ai(completion)

    def on_message_from_user(message):
        recorder_window.log(conversation.get_log())
        chat_completion.complete(conversation.get_convo())

    def on_input_from_sensor(message):
        recorder_window.log(conversation.get_log())

    def on_message_from_ai(message):
        recorder_window.log(conversation.get_log())
        actions = ActionFactory.create_actions(message)
        action_list.add_actions(actions)

    def on_recording_ready(file_path):
        transcriber.transcribe(file_path)

    def on_start_recording():
        audio_recorder.start()

    def on_stop_recording():
        audio_recorder.stop()

    def on_close():
        audio_recorder.destroy()
        robot.stop();
        # robot.disconnect()
        print('closeing app')

    # action_list_watcher = ActionListWatcher(action_list, callback=lambda action: print(f"Executing action: {action.description}"))


    action_list = ActionList()
    audio_recorder = AudioRecorder(on_recording_ready)
    transcriber = WhisperASR(on_transcription_ready)
    conversation = Conversation(on_message_from_user, on_input_from_sensor, on_message_from_ai)
    chat_completion = ChatCompletion(on_chat_completion)


    robot = VectorController(action_list)
    robot.connect()
    robot.run()

    # Launch the UI
    recorder_window = RecorderWindow(on_start_recording, on_stop_recording, on_close)
    recorder_window.run()

    # action_list_watcher.stop()

if __name__ == "__main__":
    create_app()





# import openai
# import anki_vector
# import tkinter as tk

# from action_list import ActionList
# from action import Action
# from action_list_watcher import ActionListWatcher
# from recorder_window import RecorderWindow

# openai.api_key = "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"

# def main():
#     args = anki_vector.util.parse_command_args()

#     conversation = ''



#     with anki_vector.Robot(args.serial) as robot:
#         def handle_action(action):
#             print(f"Handling action: {action.description}")

#         def handle_human_input(text):
#             print(f"Human said: {text}")
#         action_list =  ActionList()
#         action_list_watcher = ActionListWatcher(action_list, callback=handle_action)
#         action_list.add_action(Action("Turn on the light"))
#         action_list.add_action(Action("Close the door"))
#         action_list.add_action(Action("Pick up the book"))

#         root = tk.Tk()
#         recorder_window = RecorderWindow(root, action_list, callback=create_action)
#         root.mainloop()

#     print('doe')
    

# if __name__ == "__main__":
#     main()
