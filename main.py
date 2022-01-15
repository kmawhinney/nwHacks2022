import speech_recognition as sr
import pyttsx3
import datetime

print('Loading your AI personal assistant - G One')

# Microsoft Speech API 5.4 (sapi5)
engine=pyttsx3.init('')
voices=engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 190)
engine.setProperty('voice','voices[0].id')

# Text-to-speech Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant G-One")
wishMe()

if __name__=='__main__':
    print("All done")
