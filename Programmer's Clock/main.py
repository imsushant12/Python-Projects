from pygame import mixer
from time import time
from time import sleep

def getdate():
    '''To get the current date and time at time of entry'''
    import datetime
    return (str(datetime.datetime.now()))

def musicloop(stopper):
    mixer.init()
    mixer.music.load("music.mp3")
    mixer.music.play()  #playing the music provided i.e. music.mp3
    while True:
        x = input("Please type STOP to stop the alarm or EXIT to stop the program : ")
        # music termination condition.
        if (x.upper() == stopper):
            print("\nGreat! Get back to work:)\n")
            mixer.music.stop()
            return True
            break
        # program termination condition.
        elif (x.upper() == "EXIT"):
            return False

# total_hours = 2

# variables initialized with 0 for counting total number of exercises and water drank in a day
total_water = 0
total_physical_exercises = 0
total_eye_exercises = 0

if __name__ == '__main__':
    print("\n\t\t\t\tHey Programmer! This is your Health-Alarm-Clock\n")
    time_phy = time()
    time_drink = time()
    time_eyes = time()

    eyes_delay = 10     #1800 as eyes exercise should be done after half an hour
    drink_delay = 20    #3600 as water to be taken after an hour
    phy_delay = 35      #5400 as eyes exercise should be done after 1.5 hour



    while(True):
        # Drink water condition.
        if (time() - time_drink > drink_delay):
            print("Hey! Please drink some water (at least 200 ml).")

            # Checking the user input so that music can be stopped.
            if(musicloop("STOP")):
                pass
            else:
                break;

            # reinitializing the variable
            time_drink = time()
            #incrementing the value
            total_water += 200
            #opening the file and putting the data into that file
            f = open("drank.txt", "at")
            f.write("[ " + getdate() + " ] \n")
            f.close()

        # Eye exercise condition.
        if (time() - time_eyes > eyes_delay):

            print("Hey! Please do an Eye Exercise.")

            if (musicloop("STOP")):
                pass
            else:
                break;

            time_eyes = time()
            total_eye_exercises += 1
            f = open("eye.txt", "at")
            f.write("[ " + getdate() + " ] \n")
            f.close()

        # Eye exercise condition.
        if (time() - time_phy > phy_delay):
            print("Hey! Please do a Physical Exercise.")

            if (musicloop("STOP")):
                pass
            else:
                break;

            time_phy = time()
            total_physical_exercises += 1
            f = open("phy_exer.txt" , "at")
            f.write("[ " + getdate() + " ] \n")
            f.close()


    print()
    print(f"Total water taken today : {total_water}.")
    try:
        f = open("drank.txt" , "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")

    print(f"Total eye exercise done today : {total_eye_exercises}.")
    try:
        f = open("eye.txt" , "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")

    print(f"Total physical exercises done today : {total_physical_exercises}.")
    try:
        f = open("phy_exer.txt" , "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")

    sleep(5)