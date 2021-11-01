print("\t\t\t ======================")
print("\t\t\t | Rock Paper Scissor |")
print("\t\t\t ======================")


def vscomputer():
    player = input("Enter your name: ")


def vsplayer():
    player1 = input("Enter first player name: ")
    player2 = input("Enter second player name: ")


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
