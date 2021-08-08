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
engine.setProperty('voice', voices[1].id)


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
    takeCommand=takeVoiceCommand
    while True:
        # if track:
        #     time.sleep(timegap)
        #     speak("Sir, is there anything else which i can help you?")
        query = takeCommand().lower()
        # track = 1
        # logic for executing tasks based on query
        if "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q) 

        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Ani ! How May i Help you.."
            speak(hel)

        elif 'wikipedia' in query:
            speak('searching details...wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            # timegap=2

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("www.youtube.com")
            # timegap=8

        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("www.google.com")
            # timegap=8

        elif 'open github' in query:
            speak("opening github...")
            webbrowser.open("https://github.com/Anirban2001")
            # timegap=6

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")
            # timegap=8

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")
            # timegap=8

        elif 'open gmail' in query or 'open my mail' in query or 'open email' in query:
            speak("opening gmail...")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
            # timegap=8

        elif 'open amazon' in query or 'shop online' in query:
            speak("opening amazon")
            webbrowser.open("https://www.amazon.com")
            # timegap=6

        elif 'open flipkart' in query:
            speak("opening flipkart")   
            webbrowser.open("https://www.flipkart.com")
            # timegap=6

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")
            # timegap=8

        elif 'play music' in query or 'music' in query:
            speak("ok...i am playing music...")
            music_dir = 'C:\\Users\\HP\\Music\\Hindi music'
            songs = os.listdir(music_dir)
            # print(songs)                                                                                                        
            # print(len(songs))
            songNumber = random.randint(1,len(songs))
            # print(songNumber)
            os.startfile(os.path.join(music_dir,songs[songNumber]))
            # timegap=8

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            # timegap=1

        elif 'open code' in query or 'open vs code' in query:
            speak("opening vs code...")
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            # timegap=10

        elif 'send email' in query: 
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
            # timegap=2

        elif 'shutdown' in query:
            speak("are you sure?")
            confirmation=takeCommand().lower()
            if 'yes' in confirmation:
                speak("Shutting down")
                os.system("shutdown /s /t 1")
                #  Here /s is for shutdown and /r for restart and /t stands for timer and 0 indicates 0 second. Therefore after executing this program, system gets shutdown within 0 second.

        elif 'restart' in query:
            speak("are you sure?")
            confirmation=takeCommand().lower()
            if 'yes' in confirmation:
                speak("restarting")
                os.system("shutdown /r /t 1")

        elif 'exit' in query or 'goodbye' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query or 'get out' in query:
            speak("ok sir...thank you, Have a nice day...")
            break

        elif query=="none" :
            # speak("Sorry sir i did not get you...")
            # speak("please say that again...")
            # track=0
            # timegap=1
            continue
        elif 'write' in query:
            takeCommand=takeManualCommand
            speak("ok sir, input mode changed")
        elif 'speak' in query:
            takeCommand=takeVoiceCommand
            speak("ok sir, input mode changed")
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer !...please wait...'
            speak(res_g)
            webbrowser.open(g_url+temp)
        