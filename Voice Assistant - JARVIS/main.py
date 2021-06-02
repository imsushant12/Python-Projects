import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


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
    text = "Jarvis, is all ready for your commands sir. How may I help you?"
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
        r.pause_threshold = 1
        audio = r.listen(source)

        # dealing with external module hence using exception handling.
        try:
           print("Recognizing input...")
           input = r.recognize_google(audio , language='en-in')
           print(f"You said : {input}\n")

        except Exception as e:
            # print(e)
            text = "Please say it again sir."
            print(text)
            speak(text)
            return "None"
        return input


def newsReader():
    import requests
    import json

    req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=34f65666464e465a9c553b3d6445fa66")
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


# main function
if __name__ == "__main__":
    wish()

    while True:
        input = takeCommand().lower()

        # Logic behind each task execution as per the input.
        if ("day" in input or "time" in input or "date" in input):
            day_and_time()

        # Searching on wikipedia.
        elif ("wikipedia" in input):
            text = "Searching on Wikipedia sir..."
            print(text)
            speak(text)
            input = input.replace("wikipedia" , "")
            try:
                result = wikipedia.summary(input , sentences=1)
                text = "According to Wikipedia : " + result
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)

        # Opening different webpages.
        elif ("open youtube" in input):
            webbrowser.open("youtube.com")
        elif ("open google" in input):
            webbrowser.open("google.com")
        elif ("open linkedin" in input):
            webbrowser.open("linkedin.com")
        elif ("open github" in input):
            webbrowser.open("github.com")
        elif ("open gmail" in input):
            webbrowser.open("gmail.com")
        elif ("open twitter" in input):
            webbrowser.open("twitter.com")
        elif ("open facebook" in input):
            webbrowser.open("facebook.com")
        elif ("open instagram" in input):
            webbrowser.open("instagram.com")
        elif ("open flipkart" in input):
            webbrowser.open("flipkart.com")
        elif ("open amazon" in input):
            webbrowser.open("amazon.in")
        elif ("open stackoverlow" in input):
            webbrowser.open("stackoverflow.com")
        elif ("open geeksforgeeks" in input):
            webbrowser.open("geeksforgeeks.com")

        # playing music.
        elif ("play music" in input):
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

        # sending emails.
        elif ("email" in input):
            webbrowser.open("gmail.com")

        # news reading.
        elif ("news" in input):
                newsReader()

        # current location.
        elif ("location" in input):
            import geocoder
            g = geocoder.ip('me')
            speak(str(g.latlng))
            print(g.latlng)


        # opening camera
        elif ("camera" in input):
            import subprocess , time
            subprocess.run('start microsoft.windows.camera:', shell=True)
            time.sleep(10)
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


        elif ("sleep" in input or "nothing" in input or "exit" in input or "thank you" in input):
            break






'''

# send emails.
# elif ("send email"):
        #     try:
        #         text = "What is the text sir?"
        #         print(text)
        #         speak(text)
        #         message = takeCommand()
        #         text = "What is the email sir?"
        #         print(text)
        #         speak(text)
        #         email = takeCommand()
        #         text = "Are the message and email correct?"
        #         print(text)
        #         speak(text)
        #         choice = takeCommand().lower()
        #         if (choice == "yes"):
        #             sendEmail(message , email)
        #         else :
        #             text = "Sir, Please manually send the email, I am still learning."
        #             print(text)
        #             speak(text)
        #
        #     except Exception as e:
        #         # print(e)
        #         text = "Could not send it sir, can you please say it again?"
        #         print(text)
        #         speak(text)


# # function declaration
# def sendEmail(message , email):
#     """
#     This function will take email and message and then sent is to the recipient
#     """
#     server = smtplib.SMTP("smtp.gmail.com" , 587)
#     server.ehlo()
#     server.starttls()
#     server.login("sender-email_id", "sender-email_password")
#     server.sendmail("sender-email_id", email , message)
#     server.close()
#     text = "Email is sent sir!"
#     print(text)
#     speak(text)
'''