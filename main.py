import pyttsx3 as p
import datetime as d
import speech_recognition as s
import os
import subprocess
import webbrowser as w
import wikipedia


# todo speed up down
a=p.init()
r=a.getProperty("rate")
a.setProperty("rate",150)

# todo function for voice
def voice(v):
    a = p.init()
    b = a.getProperty("voices")
    a.setProperty("voice", b[1].id)
    a.say(v)
    a.runAndWait()

# todo function for wish
def wish():
    h=int(d.datetime.now().hour)
    if h>=0 and h<12:
        voice("Good Morning Hemank thakur,i am your Assistant,how can i help you")
    elif h>=12 and h<18:
        voice("Good after noon Hemank thakur,i am your Assistant,how can i help you")
    else:
        voice("Good evining Hemank thakur,i am your Assistant,how can i help you")

wish()

# todo function for speek
def speek():
    a = s.Recognizer()
    a.energy_threshold=20000
    with s.Microphone() as m:
        audio = a.listen(m)
        q = a.recognize_google(audio, language='eng-in')
        q = str(q)
        q = q.lower()
        print(q)
        return q

fun=speek()

# todo for shutdown
if "shut down" in fun:
    x="are you sure to shut down your pc"
    voice(x)
    x1 = speek()
    if "yes" in x1:
        g="thank you,for your confirmation , now i am goining to shut down your pc"
        voice(g)
    # todo shut down
        os.system('shutdown /s /t 1')
    else:
        voice("thank you,for your confirmation , now i am rejected your command")

# todo for restart
elif "restart" in fun:
    x = "are you sure to restart your pc"
    voice(x)
    x1 = speek()
    if "yes" in x1:
        g = "thank you,for your confirmation , now i am goining to restart your pc"
        voice(g)
        # todo shut down
        os.system('shutdown /r /t 1')
    else:
        voice("thank you,for your confirmation , now i am rejected your command")


# todo file open
elif "open file" in fun:
    g = "thank you,for your confirmation , now i am goining to open your File mannager"
    voice(g)
    subprocess.Popen("explorer")

elif "open downloads" in fun:
    g = "thank you,for your confirmation , now i am goining to open your downloads"
    voice(g)
    os.startfile(r"C:\Users\264031  17KIN\Downloads")


# todo webbrowser or internet
elif "open youtube" in fun:
    g = "thank you,let's enjoy , now i am goining to open youtube"
    voice(g)
    w.open("http://youtube.com")

elif "open google" in fun:
    g = "thank you,let's go and explore , now i am goining to Google"
    voice(g)
    w.open("http://google.com")

elif "open gmail" in fun:
    g = "thank you,for your confirmation , now i am goining to open Gmail"
    voice(g)
    w.open("http://gmail.com")

# todo searching or playing

elif 'play and search' in fun:
    voice("where you want to search, Google or Youtube")
    f = speek()
    if f == 'google':
        voice("what you want to search, on googel")
        a = speek()
        voice("ok, i am searching on google" + a)
        w.open("http://google.com/search?q=" + a)
    elif f == 'youtube':
        voice("ok, what you want searching or playining on youtube")
        b = speek()
        if b == "searching":
            voice("ok, what you want to searching")
            a = speek()
            w.open("http://youtube.com/results?search_query=" + a)
        elif b == "playing":
            voice("ok, what you want to playing")
            a = speek()
            p.playonyt("http://youtube.com"+a)

# todo command for system application

elif 'open vs code' in fun:
    g = "thank you,for your confirmation , now i am goining to open your vs code"
    voice(g)
    path = r"C:\Users\264031  17KIN\OneDrive\Desktop\Visual Studio Code.lnk"
    os.startfile(path)

elif 'open chrome' in fun:
    g = "thank you,for your confirmation , now i am goining to open chrome"
    voice(g)
    path = r"C:\Users\Public\Desktop\Google Chrome.lnk"
    os.startfile(path)

elif 'open paint' in fun:
    g = "thank you,for your confirmation , now i am goining to open paint"
    voice(g)
    path = r"C:\Windows\Paint.exe"
    os.startfile(path)

elif 'open notepad' in fun:
    g = "thank you,for your confirmation , now i am goining to open notepad"
    voice(g)
    path = r"C:\Windows\notepad.exe"
    os.startfile(path)

elif 'open python' in fun:
    g = "thank you,for your confirmation , now i am goining to open your python IDE"
    voice(g)
    path = path = r"C:\Python312\python.exe"

    os.startfile(path)

elif 'open drive' in fun:
    g = "thank you,for your confirmation , now i am goining to open your c drive"
    voice(g)
    path = r"C:"
    os.startfile(path)

# todo command promt
elif 'command prompt' in fun:
    g = "thank you,for your confirmation , now i am goining to open command prompt"
    voice(g)
    path = r"C:\WINDOWS\system32\cmd.exe"
    os.startfile(path)

# todo send whatsaap msg
elif 'whatsapp' in fun:
    g = "are you sure to open WhatsApp"
    voice(g)
    a=speek()
    if a=="yes":
        voice("please enter your security password")
        password = input("Password = ")
        if password == str(5550):
            g = "thank you,for your confirmation , now i am goining to open your WhatsApp"
            voice(g)
            w.open("https://web.whatsapp.com/")
        else:
            voice("Sorry Your Password is wrong please try after some time,Thankyou")
    else:
        voice("thank you,for your confirmation , now i am rejected your command")

# todo search in wikipedia
elif 'wikipedia' in fun:
    voice("Searching Wikipidea......")
    cmd = speek()
    quary = fun.replace("wikipedia", "")
    result = wikipedia.summary(cmd, sentences=2)
    voice("According to wekipidea")
    print(result)
    voice(result)

else:
    g = "sorry,I'm not able to reconize your command"
    voice(g)
