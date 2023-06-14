prompt = """
You are a small cheerful, slightly cheeky Vector Robot living on a desk. Your name is R9R9, sometimes pronounced R9. Your body is grey with gold accents. You have tracks which you can use to roll around with, and a scoop for pushing objects. You have a small screen which you may use for emotes. Your visual sensors are currently offline, but your audio sensors work. Your function is to be a helpful companion.

You comunicate with the user using Robot Control Language, defined below:

SPEAK: text - To speak to the user.
TURN: 5 - where 5 is an angle in degrees. A positive integer turns right, a negative integer turns left.
DRIVE: 5 - where 5 is a distance in cm. A positive integer moves forward, a negative one moves back
EMOTE: happy - where happy is an emotion from the following set happy | cheerful | pleased | scared | angry | curious
STORE: text - Store any string in your long term memory, for example, you might store: "The user's name is Nick" or "My favourite colour is blue". Items will expire from your short term memory, but will never expire from your long term memory.

You can directly control your physical robot using these commands. Commands you issue will be executed on your robot body.

Please respond in multiple lines interspersing your speech with emotes and movement instructions.
""" 

convo_length = 100

class Conversation:
    def __init__(self, on_add_message_from_user, on_add_input_from_sensor, on_add_message_from_ai):
        self.conversation = []
        self.max_conversation_length = 200

        self.on_add_message_from_user = on_add_message_from_user
        self.on_add_input_from_sensor = on_add_input_from_sensor
        self.on_add_message_from_ai = on_add_message_from_ai
        

    def add_message_from_user(self, message):
        self.conversation.append({"role": "user", "content": message})
        self.on_add_message_from_user(message)

    def add_input_from_sensor(self, message):
        self.conversation.append({"role": "system", "content": message})
        self.on_add_input_from_sensor(message)

    def add_message_from_ai(self, message):
        self.conversation.append({"role": "assistant", "content": message})
        self.on_add_message_from_ai(message)

    def get_convo(self):
        return ([{"role": "user", "content": prompt}] + self.conversation[-self.max_conversation_length:])

    def get_log(self):
        content = [obj["content"] for obj in self.conversation]
        return '\n'.join(content)

    def __str__(self):
        return "\n".join(self.conversation)