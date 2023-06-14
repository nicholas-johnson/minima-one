from action import EmoteAction, TalkAction

class ActionList:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def add_actions(self, actions):
        self.actions = self.actions + actions

    def get_next_action(self):
        return self.actions.pop(0) if self.actions else None

    def clear_actions(self):
        self.actions.clear()

    def __str__(self):
        return "\n".join(str(action) for action in self.actions)


if __name__ == "__main__":
    # Example usage:
    action_list = ActionList()

    # Add actions
    action_list.add_action(TalkAction("hi I'm vector"))
    action_list.add_actions([EmoteAction("Happy"), TalkAction("How are you?")])
    
    # Get and print the next action
    next_action = action_list.get_next_action()
    print(f"Next action: {next_action}")

    # Print all remaining actions
    print("Remaining actions:")
    print(action_list)

    # Clear the action list
    action_list.clear_actions()

    # Check if the action list is empty
    if not action_list.get_next_action():
        print("No more actions.")