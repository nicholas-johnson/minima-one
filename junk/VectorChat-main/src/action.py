class Action:
    pass

class TalkAction(Action):
    def __init__(self, message):
        self.message = message


class EmoteAction(Action):
    def __init__(self, emotion):
        self.emotion = emotion

class DriveAction(Action):
    def __init__(self, distance):
        self.distance = distance

class TurnAction(Action):
    def __init__(self, angle):
        self.angle = angle
