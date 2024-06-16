import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! sir")

    else:
        speak("Good Evening! sir")

    # speak("I am friday Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am Listening sir ...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('stharabi9862187405@gmail.com', to, content)
    server.close()


friday = True

if __name__:
    '__main__'
while True:
    query = str(takeCommand()).lower()
    if 'friday' in query:
        wishMe()
        friday = True
        speak("I am on your command sir")
        while friday:
            query = str(takeCommand()).lower()
            if 'wikipedia' in query:
                speak("ok sir")
                speak(',Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                friday = False

            elif 'open youtube' in query:
                speak("ok sir, opening youtube")
                webbrowser.open("youtube.com")
                friday = False

            elif 'open google' in query:
                speak("ok sir,opening google")
                webbrowser.open("google.com")
                friday = False

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                friday = False

            elif 'play music' in query:
                playsound('C:\\Users\\Lenovo\\Downloads\\alarm.wav')
                # music_dir = 'C:\\Users\\Lenovo\\Downloads\\alarm.wav'
                # songs = os.listdir(music_dir)
                # print(songs)
                # os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                speak("ok Sir")
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                speak(f"Sir, the time is {strTime}")
                friday = False

            elif 'open code' in query:
                codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                friday = False

            elif 'email to Ravi' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "harryyourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                    friday = False
                except Exception as e:
                    print(e)
                    speak("Sorry sir i can't send email")

            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")

            elif 'restart' in query:
                speak("ok Sir")
                speak("Computer is restarting..")
                os.system("shutdown /r /t 1")
    else:
        speak("have a nice day sir ")
