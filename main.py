import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia



print('Loading your financial personal assistant - G One')

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 190)


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

speak("Loading your financial personal assistant G-One")
wishMe()

if __name__=='__main__':
    print("All done")

    while True:
        speak("Tell me how can I help you now?")
        speak("For specific Company information say Company Information")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break
            
        if 'explain' in statement:
            speak('Searching...')
            statement =statement.replace("explain", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            continue

        if 'company information' in statement:
            speak('Say Company Name')
            company_name = takeCommand().lower()
            speak('Say information needed, options are Quotes, Market Summary, Option Chain information ') #work on summary
            information_parameter = takeCommand().lower()
            if 'quotes' in information_parameter:
                continue
            if 'market summary' in information_parameter:
                continue
            if 'option chain information' in information_parameter:
                continue
            if 'market cap' in information_parameter:
                continue




