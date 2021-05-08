import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else :
        speak("Good evening")

    speak("i am alexa sir.how may i help u")


def takeCommand():      #it returns audio into string
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}")

    except Exception as e:
        #print(e)
        print("Say again..")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    while True:

        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            speak('according to wikipedia..')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open vs code' in query:
            codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open amazon' in query:
            webbrowser.open('amazon.in')
        
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

