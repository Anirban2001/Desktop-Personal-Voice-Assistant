import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

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
        print("Say that again please...")
        return "None"
    return query

# def takeCommand():
    # pass
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('deyanirban977@gmail.com','1161087708')
    server.sendmail('deyanirban977@gmail.com',to,content)
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
    while True:
        if track:
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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\OLD BANGLA'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query: 
            try:
                speak("Sir, please enter the mail id to whom you want to send the mail")
                to = input("Enter the mail id: ")
                speak("what should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry baban sir, I am not able to send this email")

        elif 'exit' in query:
            speak("ok sir...thank you")
            break
        else :
            speak("Sorry sir i did not get you...")
        