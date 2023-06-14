import anki_vector
from anki_vector.util import degrees
import threading
from time import sleep
from action_list import ActionList
from action import TalkAction, EmoteAction

class VectorController:
    def __init__(self, action_list, check_interval=0.1):
        self.vector = None
        self._lock = threading.Lock()
        self.action_list = action_list
        self._stop_event = threading.Event()
        self.check_interval = check_interval

    def connect(self, max_retries=5):
        retries = 0

        with self._lock:
            while retries < max_retries:
                try:
                    self.vector = anki_vector.Robot()
                    self.vector.connect()
                    break
                except:
                    retries += 1
                    print(f"Connection attempt {retries} failed. Retrying...")

            if retries == max_retries:
                print("Maximum retries reached. Connection failed.")

        print(self.vector.anim.anim_trigger_list)

    def disconnect(self):
        if self.vector:
            self.vector.disconnect()
            self.vector = None

    def run(self):
        self._watcher_thread = threading.Thread(target=self._run)
        self._watcher_thread.start()

    def _run(self,):
        while not self._stop_event.is_set():
            with self._lock:
                action = self.action_list.get_next_action()
                if action:
                    self.act(action)

            sleep(self.check_interval)

    
    def stop(self):
        self._stop_event.set()
        self._watcher_thread.join()

    def talk(self, message):
        if self.vector:
            self.vector.behavior.say_text(message)

    def emote(self, emotion):
        if self.vector:
            anim_name = "GreetAfterLongTime"
            self.vector.anim.play_animation_trigger(anim_name)

    def act(self, action):
        if isinstance(action, TalkAction):
            self.talk(action.message)
        elif isinstance(action, EmoteAction):
            self.emote(action.emotion)


if __name__ == "__main__":
    action_list = ActionList()
    action_list.add_action(TalkAction("Hello, I am Vector!"))

    controller = VectorController(action_list)
    controller.connect()
    controller.run()

    action_list.add_action(TalkAction("I am Happy!"))
    action_list.add_action(EmoteAction('happy'))

    # controller.stop()
    # controller.disconnect()
