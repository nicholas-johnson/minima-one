import re

class RCLInterpreter:
    def __init__(self):
        self.commands = []

    def parse(self, text):
        lines = text.strip().split('\n')
        for line in lines:
            self.parse_line(line)

    def parse_line(self, line):
        line = line.strip()
        if line.startswith("TURN:") or line.startswith("DRIVE:") or line.startswith("EMOTE:") or line.startswith("STORE:"):
            self.commands.append(line)
        else:
            self.parse_speech(line)

    def parse_speech(self, speech):
        parts = re.split(r'(\*.*?\*)', speech)
        for part in parts:
            if part.startswith('*') and part.endswith('*'):
                emote = f'EMOTE: {part[1:-1]}'
                self.commands.append(emote)
            else:
                self.commands.append(f'SPEAK: {part}')

    def execute(self):
        for command in self.commands:
            print(f'Executing: {command}')

if __name__ == '__main__':
    rcl = RCLInterpreter()
    rcl.parse("""
Hello *world*
TURN: 5
DRIVE: 5
EMOTE: happy
STORE: text
""")
    rcl.execute()

This code defines a class RCLInterpreter that can parse and execute Robot Control Language commands. It can handle plain text, as well as commands like TURN, DRIVE, EMOTE, and STORE. Additionally, it can parse text with embedded emotes surrounded by asterisks.

You can modify the execute method to perform the desired actions for each command, e.g., controlling a robot or handling emotes.
