import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello sir how may i help you")        


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return"None"
    return query
         
            

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'hello' in query:
            speak('hello sir what should i do')

        elif 'what can you do' in query:
            speak('i can search anything for you open your dekstop apps tell the current time open social media websites and many more')

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("twitter.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open intellij idea' in query:
            codePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1\\bin\\idea64.exe"
            os.startfile(codePath)

        elif 'open lion' in query:
            codePath = "C:\\Program Files\\JetBrains\\CLion 2020.1.1\\bin\\clion64.exe"
            os.startfile(codePath)

        elif 'open proton vpn' in query:
            codePath = "C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"
            os.startfile(codePath)

        elif 'open tor browser' in query:
            codePath = "C:\\Users\\Admin\\Downloads\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(codePath)

        elif 'open quick heal' in query:
            codePath = "C:\\Program Files\\Quick Heal\\Quick Heal Total Security\\SCANNER.EXE"
            os.startfile(codePath)

        elif 'launch shutdown pc' in query:
            codePath = "C:\\Users\\Admin\\Documents\\shutdown PC.bat"
            os.startfile(codePath)

        

        
