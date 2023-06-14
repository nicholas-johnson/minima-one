# Vector Chat

## Installation concerns

The Anki Vector SDK is only compatible with Python 3.8 (possibly 3.75). Higher than this will cause an arror with a loop parameter in AsyncIO. It's also not compatible with newer versions of Protobuff. Do not attempt to upgrade past 3.20.1.

```
pip3 install openai
pip3 install protobuf==3.20.1
pip3 install anki_vector
```

For audio capture (OSX) - EDIT: We use sounddevice now, so this step may not be necessary

```
brew install portaudio 
pip3 install --no-binary :all: pyaudio
```

## Running

python3 src/main.py

If you get a timeout exception on vector, try again. Note you must be running a Wirepod hacked vector in order to connect the SDK to the machine.