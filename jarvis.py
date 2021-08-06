import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import time
import random
import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir, I am here to help you")

def takeManualCommand():
    query = input("write: ")
    return query

def takeVoiceCommand():
    """
    it takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        # print("Say that again please...")
        return "None"
    return query

# def takeCommand():
    # pass
def sendEmail(mymail,password,to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    
    server.login(mymail,password)
    server.sendmail(mymail,to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    speak("do you want to say or write?")
    speak("Enter 1 for say or 2 for write")
    z = int(input("Enter: "))
    if z==1:
        speak("Okk sir...thank you, Please tell how can i help you?")
        takeCommand = takeVoiceCommand
    elif z==2:
        speak("Okk sir...thank you, Please write how can i help you?")
        takeCommand = takeManualCommand
    else:
        speak("Wrong input sir! So by default i am taking manual command")
        speak("Please write how can i help you?")
        takeCommand = takeManualCommand
    track = 0
    timegap = 2
    while True:
        if track:
            time.sleep(timegap)
            speak("Sir, is there anything else which i can help you?")
        query = takeCommand().lower()
        track = 1
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            timegap=2

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")
            timegap=8

        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("google.com")
            timegap=8

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
            timegap=8

        elif 'play music' in query:
            speak("playing music...")
            music_dir = 'C:\\Users\\HP\\Music\\Hindi music'
            songs = os.listdir(music_dir)
            # print(songs)                                                                                                        
            # print(len(songs))
            songNumber = random.randint(1,len(songs))
            # print(songNumber)
            os.startfile(os.path.join(music_dir,songs[songNumber]))
            timegap=8

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            timegap=1

        elif 'open code' in query:
            speak("opening vs code...")
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            timegap=10

        elif 'email' in query: 
            try:
                speak("Sir, please enter the mail id to whom you want to send the mail")
                to = input("Enter the mail id: ")
                speak("Sir, please enter your mail id from which you want to send the mail...")
                mymail = input("Enter your mail id: ")
                speak("Enter password: ")
                # password = input("Enter password: ")
                password = getpass.getpass(prompt = 'Enter password: ')
                speak("what should I say?")
                content = takeCommand()
                sendEmail(mymail,password,to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, I have not access to your mail id...")
            timegap=2

        elif 'exit' in query:
            speak("ok sir...thank you, Have a nice day...")
            break
        else :
            speak("Sorry sir i did not get you...")
            speak("please say that again...")
            track=0
            timegap=1
        