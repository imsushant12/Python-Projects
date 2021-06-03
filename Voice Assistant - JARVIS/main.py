import pyttsx3                       # for text to audio conversion
import datetime                      # for obtaining date and time
from datetime import date
import speech_recognition as sr      # for speech recognition and conversion to string
import wikipedia                     # for searching on wikipedia
import webbrowser                    # for opening a webpage in browser
import os                            # for reaching to a certain path
import random                        # for picking random number
import pyautogui                     # for taking screenshot
import requests                      # for making API requests
import json                          # for parsing data
from bs4 import BeautifulSoup        # for weather forecasting
import subprocess , time             # for opening windows applications and closing the, after certain interval




# Text to speech using pyttsx3 module.
engine = pyttsx3.init()
def speak(text):
    """
    This function will convert given text to audio and plays it.
    """
    # engine.setProperty("rate", 200)
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


def wish():
    """
    This function will wish the user according to the time
    and ask for further commands.
    """
    hour = datetime.datetime.now().hour
    if (hour < 12):
        text = "Good morning sir!"
        print(text)
        speak(text)
    elif (hour >= 12 and hour <= 18):
        text = "Good afternoon sir!"
        print(text)
        speak(text)
    else:
        text = "Good evening sir!"
        print(text)
        speak(text)
    text = "JARVIS, is all ready for your commands sir. How may I help you?"
    print(text)
    speak(text)


def day_and_time():
    """
    This function will tell current date and time as per the user input.
    """
    today = str(date.today())
    text = "Sir Today's date is : " + today
    print(text)
    speak(text)

    from datetime import datetime
    time = datetime.today().strftime("%I:%M %p")
    text = "And current time is : " + time
    print(text)
    speak(text)


def takeCommand():
    """
    This function takes microphone input from user and returns a string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        # giving some time before considering it as final input.
        # r.pause_threshold = 1
        audio = r.listen(source , 5 , 5)

        # dealing with external module hence using exception handling.
        try:
           print("Recognizing input...")
           input = r.recognize_google(audio , language = "en-in")
           print(f"You said : {input}\n")

        except Exception as e:
            # print(e)
            text = "Please say it again sir."
            print(text)
            speak(text)
            return "None"
        return input


def newsReader():
    """
    This function will tell top 5 news headlines using API and json module.
    """

    req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=(OWN API PROVIDED BY WEBSITE)")
    dict = json.loads(req.text)

    text = "Top 5 News for today are:\n"
    print(text)
    speak(text)

    counter = 5
    arts = dict['articles']
    for i in arts:
        if(counter > 0):
            print("The Headline is - " + str(i["title"]))
            speak("The Headline is - " + str(i["title"]))

            print("Story - " + str(i["description"]))
            speak(i["description"])

            print("Checkout the link for detail : " + str(i['url']))
            speak("Moving to the next news...")

            counter -= 1


def there_exists(terms):
    """
    Function to check if required word or phrase is present in the text or not.
    """
    for term in terms:
        if term in input:
            return True



def details():
    """
    This function will print and speak written text.
    """
    text = "Hello sir! I am JARVIS. I am a virtual assistant created by SUSHANT sir. " \
           "You can check the things that I can do by saying 'what can you do' or 'things you can do'"
    print(text)
    speak(text)



def jarvisWork():
    """
        This function will print and speak written text.
    """
    text = "Sir, I can open numerous applications and webpages, play games, take screenshots, tell you time, date, weather, location and " \
           "can read news headlines, flip coin , search on spotify, google, youtube and wikipedia. I can also calculate, take notes etc." \
           "I am still learning new things from wonderful humans like you. Nice knowing your sir."
    print(text)
    speak(text)




# main function
if __name__ == "__main__":
    wish()

    while True:
        input = takeCommand().lower()

        # Greetings.
        if there_exists(["hi" , "hello" , "hey" , "jarvis you there"]):
            text = "Hello! JARVIS at your service sir."
            print(text)
            speak(text)


        elif there_exists(["how are you" , "how you doing" , "whats up"]):
            text = "Hello! Thanks for asking! I am good sir and all ready at your service sir"
            print(text)
            speak(text)


        # Assistant Details.
        elif there_exists(["who are you" , "who made you" , "what is your name"]):
            details()


        # Things that JARVIS can do.
        elif there_exists(["what can you do" , "things you can do"]):
            jarvisWork()


        # Logic behind each task execution as per the input.
        elif there_exists(["day","date","time"]):
            day_and_time()


        # Searching on wikipedia.
        elif ("wikipedia" in input):
            text = "Searching on Wikipedia sir..."
            print(text)
            speak(text)
            input = input.replace("wikipedia" , "")
            try:
                result = wikipedia.summary(input , sentences=1)
                text = "Sir According to Wikipedia : " + result
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on google
        elif there_exists(["search google" , "google search" , "search on google"]):
            text = "Searching on Google sir..."
            print(text)
            speak(text)
            search_term = input.split("google")[-1]
            try:
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
                text = "This is what I found on Google sir."
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on spotify
        elif there_exists(["search spotify" , "spotify search"]):
            text = "Searching on Spotify sir..."
            print(text)
            speak(text)
            search_term = input.split("spotify")[-1]
            try:
                url = "https://open.spotify.com/search/"+search_term
                webbrowser.get().open(url)
                text = "This is what I found on Spotify sir."
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on youtube
        elif there_exists(["search youtube" , "search on youtube"]):
            text = "Searching on Youtube sir..."
            print(text)
            speak(text)
            search_term = input.split("youtube")[-1]
            try:
                url = "https://www.youtube.com/results?search_query=" + search_term
                text = "This is what I found on Youtube sir."
                print(text)
                speak(text)
                webbrowser.get().open(url)
            except Exception as e:
                 # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Opening different webpages.
        elif ("open youtube" in input):
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)
        elif ("open google" in input):
            url = "https://www.google.com/"
            webbrowser.get().open(url)
        elif ("open linkedin" in input):
            url = "https://www.linkedin.com/"
            webbrowser.get().open(url)
        elif ("open github" in input):
            url = "http://github.com/"
            webbrowser.get().open(url)
        elif ("open gmail" in input):
            url = "http://gmail.com/"
            webbrowser.get().open(url)
        elif ("open twitter" in input):
            url = "https://twitter.com/"
            webbrowser.get().open(url)
        elif ("open facebook" in input):
            url = "https://www.facebook.com/"
            webbrowser.get().open(url)
        elif ("open instagram" in input):
            url = "https://www.instagram.com/"
            webbrowser.get().open(url)
        elif ("open flipkart" in input):
            url = "https://www.flipkart.com/"
            webbrowser.get().open(url)
        elif ("open amazon" in input):
            url = "https://www.amazon.in/"
            webbrowser.get().open(url)
        elif ("open stack overlow" in input):
            url = "https://stackoverflow.com/"
            webbrowser.get().open(url)
        elif ("open geeksforgeeks" in input):
            url = "https://www.geeksforgeeks.org/"
            webbrowser.get().open(url)


        # playing music.
        elif there_exists(["play" , "music" , "play music" , "song"]):
            musicFolder = "D:\\Music"
            allSongs = os.listdir(musicFolder)
            choice = random.choice(allSongs)
            os.startfile(os.path.join(musicFolder , choice))


        # opening coding platforms (IDEs) and other applications.
        elif ("open code blocks" in input):
            location = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(location)
        elif ("open visual studio" in input or "open vs code" in input):
            location = "C:\\Users\\susha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(location)
        elif ("open git" in input):
            location = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(location)
        elif ("open pycharm" in input):
            location = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(location)
        elif ("open netbeans" in input):
            location = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
            os.startfile(location)
        elif ("open chrome" in input):
            location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(location)
        elif ("open word" in input):
            location = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(location)
        elif ("open excel" in input):
            location = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(location)
        elif ("open powerpoint" in input):
            location = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(location)
        elif ("open adobe" in input):
            location = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(location)
        elif ("open notepad" in input):
            location = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(location)


        # opening emails (inbox).
        elif there_exists(["mails" , "mail" , "my email" , "my emails"]):
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            text = "Here are your mails sir."
            print(text)
            speak(text)


        # news reading.
        elif ("news" in input):
                newsReader()


        # current location.
        elif ("location" in input):
            import geocoder
            g = geocoder.ip('me')
            speak(str(g.latlng))
            print(g.latlng)


        # Opening camera
        elif ("camera" in input):
            subprocess.run('start microsoft.windows.camera:', shell=True)
            time.sleep(11)
            text = "Sir it will automatically close after 11 seconds."
            print(text)
            speak(text)
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


        # make a note
        elif there_exists(["make a note" , "take a note" , "take note" , "takes notes"]):
            text = "Opening note taker..."
            print(text)
            speak(text)
            try:
                url = "https://keep.google.com/#home"
                text = "Note taker opened sir."
                print(text)
                speak(text)
                webbrowser.get().open(url)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Take screenshot
        elif there_exists(["capture" , "capture screen" , "take screenshot" , "screenshot"]):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("D:\Python\\" + "_Jarvis_screenshot.png")
            text = "Screenshot taken sir."
            print(text)
            speak(text)



        # Play Rock , Paper , Scissor Game
        elif there_exists(["game" , "play a game" , "rock paper scissor"]):
            text = "Please choose among rock, paper and scissor"
            print(text)
            speak(text)

            pmove = takeCommand()

            moves = ["rock", "paper", "scissor"]
            cmove = random.choice(moves)

            if pmove == cmove:
                text = "the match is draw"
                print(text)
                speak(text)
            elif (pmove == "rock" and cmove == "scissor") or (pmove == "paper" and cmove == "rock") or (pmove == "scissor" and cmove == "paper"):
                text = "Player wins"
                print(text)
                speak(text)
            elif (pmove == "scissor" and cmove == "rock") or (pmove == "rock" and cmove == "paper") or ("paper" and cmove == "scissor"):
                text = "Computer wins"
                print(text)
                speak(text)


        # Weather Forecasting.
        elif there_exists(["temperature" , "weather" , "what is the weather" , "how is the weather"]):
            try :
                url = "https://google.com/search?q=" + input
                r = requests.get(url)
                data = BeautifulSoup(r.text , "html.parser")
                weather = data.find("div" , class_="BNeawe").text
                output = "Current weather is : " + weather
                print(output)
                speak(output)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Toss a coin
        elif there_exists(["toss" , "flip" , "coin"]):
            moves = ["head" , "tails"]
            choice = random.choice(moves)
            text = "Sir we have got : " + choice
            print(text)
            speak(text)

        # Calculations.
        elif there_exists(["calculate" , "plus" , "minus" , "add" , "subtract" , "multiply" , "divide" ,
                           "+" , "-" , "*" , "/" , "power" or "**"]):
            try:
                value = input.split()[1]
                if value == '+' or value == "add" or value == "plus":
                    speak(int(input.split()[0]) + int(input.split()[2]))
                elif value == '-' or value == "minus" or value == "subtract":
                    speak(int(input.split()[0]) - int(input.split()[2]))
                elif value == 'multiply':
                    speak(int(input.split()[0]) * int(input.split()[2]))
                elif value == 'divide':
                    speak(int(input.split()[0]) / int(input.split()[2]))
                elif value == 'power':
                    speak(int(input.split()[0]) ** int(input.split()[2]))
                else:
                    speak("Wrong Operator")
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)

        # About creator.
        elif there_exists(["creator", "sushant"]):
            text = '''
                    Sushant is a Junior year student, pursuing bachelors in Computer Science and Engineering. 
                    He am a pragmatic programmer who loves to create major and minor projects infact 
                    I am also one of his projects made in Python. 

                    He is a Technical Content Writer Intern at GeeksForGeeks and a participant contributing to 
                    open-source projects in GirlScript Summer of Code, 2021 and Let's Grow More Summer of Code, 2021.

                    He isalso a Microsoft Learn Student Ambassador currently at Beta Level. 
                    He is a Software Developer with an experience in C , C plus plus , Python, Data Structures, 
                    Algorithm, Technical Content Writing and Front End Web Development.
                    '''
            speak(text)

        # Terminating JARVIS.
        elif there_exists(["sleep" , "nothing" , "bye" , "exit" , "quit" , "thank you"]):
            text = "Bye. See you soon sir. Take care!"
            print(text)
            speak(text)
            break




