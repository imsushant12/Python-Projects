import random

print("\t\t\t ======================")
print("\t\t\t | Rock Paper Scissor |")
print("\t\t\t ======================")


def check(choice1, choice2):
    if choice1 == "rock":
        if choice2 == "scissor":
            return 1
        else:
            return 0

    elif choice1 == "paper":
        if choice2 == "rock":
            return 1
        else:
            return 0
    else:
        if choice2 == "paper":
            return 1
        else:
            return 0


def vscomputer():
    choices = ["rock", "paper", "scissor"]
    player = input("Enter your name: ")
    userchoice = input("""
            What you want to choose? 
                rock
                paper
                scissor  : """)
    computerchoice = random.choice(choices)

    if(computerchoice.lower() == userchoice.lower()):
        print("It's a tie!")

    elif check(userchoice.lower(), computerchoice.lower()) == 1:
        print(f"{player}! You have WON the game as computer chose {computerchoice}")
    else:
        print(f"{player}! You have LOST the game as computer chose {computerchoice}")


def vsplayer():
    player1 = input("Enter first player name: ")
    player2 = input("Enter second player name: ")
    player1choice = input(f"""
            What you want to choose {player1} ? 
                rock
                paper
                scissor  : """)
    player2choice = input(f"""
            What is your choice {player2} ? 
                rock
                paper
                scissor  : """)

    if(player1choice.lower() == player2choice.lower()):
        print("It's a tie!")

    elif check(player1choice.lower(), player2choice.lower()) == 1:
        print(f"{player1}! You have WON the game!!!")
    else:
        print(f"{player2}! You have WON the game!!!")


print('''
    Options to play:
    1. With computer.
    2. With other player.
    ''')

choice = int(input("Enter your choice: "))


if choice == 1:
    vscomputer()
else:
    vsplayer()
