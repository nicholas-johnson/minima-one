import re
from action import EmoteAction, TalkAction, DriveAction, TurnAction

class ActionFactory:
    @staticmethod
    def create_actions(str):
        actions = []

        pattern = r"(EMOTE:|SPEAK:|DRIVE:|TURN:)"

        print(str)
        split_list = re.split(pattern, str)
        filtered_list = [s for s in split_list if s.strip()]   
        action_strings = [filtered_list[i] + filtered_list[i + 1] for i in range(0, len(filtered_list), 2)]
        action_strings = [s.strip() for s in action_strings]

        print(action_strings)

        for action_string in action_strings:
            if action_string.strip() == "":
                continue

            if action_string.strip().startswith("SPEAK:"):
                actions.append( TalkAction(action_string) )
                continue

            if action_string.strip().startswith("EMOTE:"):
                actions.append( EmoteAction(action_string))
                continue

            if action_string.strip().startswith("DRIVE_FORWARD"):
                actions.append( DriveAction(action_string))
                continue

            if action_string.strip().startswith("DRIVE_BACKWARD"):
                actions.append( DriveAction(action_string))
                continue

            if action_string.strip().startswith("TURN_LEFT:"):
                actions.append( TurnAction(action_string))
                continue

            if action_string.strip().startswith("TURN_RIGHT:"):
                actions.append( TurnAction(action_string))
                continue

            actions.append( TalkAction(action_string) )

        return actions


if __name__ == "__main__":
    action_str = """
    SPEAK: hello EMOTE: happy
    SPEAK: Cats
    """

    actions = ActionFactory.create_actions(action_str)

    print(f"Actions: {actions}")
