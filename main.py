import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Microsoft Speech API 5.4 (sapi5)
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
