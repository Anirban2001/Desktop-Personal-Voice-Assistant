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
import pywhatkit

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

    speak("I am Jarvis sir,how can i help you?")


def takeManualCommand():
    query = input("write: ")
    return query

fg=0
def takeVoiceCommand():
    global fg
    """
    it takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    # device_index=0
    with sr.Microphone() as source: 
        if fg==0:
            print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        # print("Recognizing...")
        print(f"user said: {query}\n")
        fg=0
    except Exception as e:
        fg=1
        return "None"

    return query


def sendEmail(mymail, password, to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(mymail, password)
    server.sendmail(mymail, to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    takeCommand = takeVoiceCommand
    # takeCommand=takeManualCommand
    while True:
        query = takeCommand().lower()
        if "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!',
                      'I am nice and full of energy', 'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)

        elif "hello" in query or "hello Jarvis" in query:
            hel = "yes sir, i am here..."
            speak(hel)

        elif 'wikipedia' in query:
            speak('searching details...wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("www.youtube.com")

        elif 'youtube' in query:
            content = query.replace('play', '')
            print(content)
            content = content.replace('youtube', '')
            print(content)
            content = content.replace(' in ', ' ')
            print(content)
            content = content.replace(' form ', ' ')
            speak("playing" + content)
            pywhatkit.playonyt(content)

        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("www.google.com")

        elif 'close chrome' in query or 'close google' in query:
            speak("chrome closed")
            os.system("taskkill /f /im chrome.exe")
        
        elif 'send whatsapp message' in query:
            try:
                pywhatkit.sendwhatmsg_instantly(phone_no="+919641152624",message="hii i am jarvis",tab_close=True)
                speak("Successfully sent!")
            except:
                speak("Sorry sir, there is some error")

        elif 'convert text to handwriting' in query:
            try:
                pywhatkit.text_to_handwriting(string="hello.\n i am Anirban Dey",save_to="x.png",rgb=(0,0,138))
                speak("handwritten saved")
            except:
                speak("some error occured")

        elif 'open github' in query:
            speak("opening github...")
            webbrowser.open("https://github.com/Anirban2001")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com/")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")

        elif 'open gmail' in query or 'open my mail' in query or 'open email' in query:
            speak("opening gmail...")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open amazon' in query or 'shop online' in query:
            speak("opening amazon")
            webbrowser.open("https://www.amazon.com")

        elif 'open flipkart' in query:
            speak("opening flipkart")
            webbrowser.open("https://www.flipkart.com")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif 'open whatsapp' in query:
            speak("opening whatsapp...")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'class schedule' in query:
            speak("here is your today's class schedule")
            webbrowser.open("https://calendar.google.com/calendar/u/3/r")

        elif 'open gsuite mail' in query or 'gsuite' in query or 'g suite' in query:
            speak("opening")
            webbrowser.open("https://mail.google.com/mail/u/3/#inbox")

        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open(
                "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'open superset' in query or 'superset' in query:
            speak("opening superset")
            webbrowser.open("https://app.joinsuperset.com/#/s/feed")

        elif 'play music' in query or 'play some music' in query:
            speak("ok...i am playing music...")
            music_dir = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            # print(len(songs))
            songNumber = random.randint(1, len(songs))
            # print(songNumber)
            os.startfile(os.path.join(music_dir, songs[songNumber]))

        elif 'stop music' in query or 'close music' in query:
            speak("music stopped")
            os.system("taskkill /f /im PotPlayerMini64.exe")

        elif 'change music' in query or 'change the song' in query:
            speak("music changed")
            os.system("taskkill /f /im PotPlayerMini64.exe")
            music_dir = 'C:\\Users\\HP\\Music'
            songs = os.listdir(music_dir)
            songNumber = random.randint(1, len(songs))
            os.startfile(os.path.join(music_dir, songs[songNumber]))

        elif 'play video' in query or 'open video' in query:
            speak("ok...i am playing video...")
            video_dir = 'G:\\folder\\New folder (5)\\New folder (5)\\New folder'
            videos = os.listdir(video_dir)
            videoNumber = random.randint(1, len(videos))
            os.startfile(os.path.join(video_dir, videos[videoNumber]))

        elif 'stop video' in query or 'close video' in query:
            speak("video closed")
            os.system("taskkill /f /im PotPlayerMini64.exe")
        
        elif 'change video' in query or 'change the video' in query:
            speak("video changed")
            os.system("taskkill /f /im PotPlayerMini64.exe")
            video_dir = 'G:\\folder\\New folder (5)\\New folder (5)\\New folder'
            videos = os.listdir(video_dir)
            videoNumber = random.randint(1, len(videos))
            os.startfile(os.path.join(video_dir, videos[videoNumber]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"sir, it is {strTime}")

        elif 'open code' in query or 'open vs code' in query:
            speak("opening vs code...")
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("Sir, please enter the mail id to whom you want to send the mail")
                to = input("Enter the mail id: ")
                speak(
                    "Sir, please enter your mail id from which you want to send the mail...")
                mymail = input("Enter your mail id: ")
                speak("Enter password: ")
                password = getpass.getpass(prompt='Enter password: ')
                speak("what should I say?")
                content = takeCommand()
                sendEmail(mymail, password, to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir, I have not access to your mail id...")

        elif 'shutdown' in query:
            speak("are you sure?")
            concent = takeCommand().lower()
            if 'yes' in concent or 'ok' in concent:
                speak("Shutting down")
                os.system("shutdown /s /t 1")
                #  Here /s is for shutdown and /r for restart and /t stands for timer and 0 indicates 0 second. Therefore after executing this program, system gets shutdown within 0 second.

        elif 'restart' in query:
            speak("are you sure?")
            concent = takeCommand().lower()
            if 'yes' in concent:
                speak("restarting")
                os.system("shutdown /r /t 1")

        elif 'exit' in query or 'goodbye' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query or 'get out' in query:
            speak("ok sir...thank you, Have a nice day...")
            break

        elif query == "none":
            continue

        elif 'write' in query:
            takeCommand = takeManualCommand
            speak("ok sir, input mode changed")

        elif 'speak' in query:
            takeCommand = takeVoiceCommand
            speak("ok sir, input mode changed")

        elif 'show movie' in query or 'movie' in query:
            path = "G:\movie"
            os.startfile(path)

        elif 'show web series' in query or 'web series' in query:
            path = "G:\web series"
            os.startfile(path)

        else:
            temp = query.replace(' ', '+')
            # g_url = "https://www.google.com/search?q="
            # res_g = 'sorry! i can\'t understand...may i search in google?'
            res = 'sorry! i can\'t understand...'
            speak(res)
            # concent = takeCommand().lower()
            # if 'yes' in concent or 'ok' in concent:
            #     speak("please wait sir...i am searching...")
            #     webbrowser.open(g_url+temp)
            # elif 'no' in concent:
            #     speak("ok")
