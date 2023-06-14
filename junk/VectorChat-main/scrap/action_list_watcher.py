import threading
import time

from action_list import ActionList
from action import Action

class ActionListWatcher:
    def __init__(self, action_list, callback, check_interval=1.0):
        self.action_list = action_list
        self.callback = callback
        self.check_interval = check_interval
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._watcher_thread = threading.Thread(target=self._watch_action_list)
        self._watcher_thread.start()

    def _watch_action_list(self):
        while not self._stop_event.is_set():
            with self._lock:
                action = self.action_list.get_next_action()
                if action:
                    print(f"Executing action: {action.description}")
                    self.callback(action)

            time.sleep(self.check_interval)

    def stop(self):
        self._stop_event.set()
        self._watcher_thread.join()


# # Example usage:
# action_list = ActionList()

# # Add actions
# action_list.add_action(Action("Turn on the light"))
# action_list.add_action(Action("Close the door"))
# action_list.add_action(Action("Pick up the book"))

# # Create and start the watcher
# watcher = ActionListWatcher(action_list)

# # Add more actions after a delay
# time.sleep(5)
# action_list.add_action(Action("Read the book"))

# # Wait for a while and then stop the watcher
# time.sleep(10)
# watcher.stop()