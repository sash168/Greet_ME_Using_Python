import pyttsx3 
import datetime
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")# we can H or 
    speak("The current time is")
    speak(Time)


def date_():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    date= datetime.datetime.now().day
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sash")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning maam")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon maam")
    elif hour >= 18 and hour < 24:
        speak("Good  evening maam")
    else:
        speak("Good night maam")

    speak("Your AI assistant is in your service, please tell me how can i help you today?")

wishme()
