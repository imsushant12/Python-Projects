from random import choice

print("\t\t\t\t\t\t\t ===============")
print("\t\t\t\t\t\t\t | Tic Tac Toe |")
print("\t\t\t\t\t\t\t ===============\n")


board = [
    [" 1 ", " 2 ", " 3 "],
    [" 4 ", " 5 ", " 6 "],
    [" 7 ", " 8 ", " 9 "],
]


def check(user_input, board):
    for i in board:
        for j in i:
            pass


def print_board(board):
    print("\n=======================")
    for i in board:
        print("||", end=" ")
        for j in i:
            print(j, end=" || ")
        print("\n=======================")


def valid_places(user_input, available_choices):
    if user_input in range(1, 10) and user_input not in available_choices:
        return True
    else:
        return False


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not valid number")
        return True
    else:
        return False


def check_input(user_input, available_choices):
    if not isnum(user_input):
        return False
    else:
        if valid_places(user_input, available_choices):
            return True
        else:
            return False


def vscomputer(player, board):
    available_choices = []
    user_won = True
    while True:
        user_input = int(input("Choose your position: "))
        if check_input(user_input, available_choices):
            if check(user_input, board):
                break
            
            available_choices.append(user_input)

            computerchoice = choice(
                [i for i in range(1, 10) if i not in available_choices])

            if check(computerchoice, board):
                user_won = False

            available_choices.append(computerchoice)

        else:
            print("Incorrect choice, try again!")
    
    if user_won:
        print(f"{player}, you won the game!!!")
    else:
        print("Computer, won the game!!!")


def vsplayer(player1, player2):
    available_choices = []

    user1_won = True
    while True:
        choice1 = int(input(f"{player1}, enter your choice: "))
        if check_input(choice1, available_choices):
            if check(choice1, board):
                break
            available_choices.append(choice1)

        choice2 = int(input(f"{player2}, enter your choice: "))
        if check_input(choice2, available_choices):
            if check(choice2, board):
                user1_won = False
                break
            available_choices.append(choice2)
        else:
            print("Incorrect choice, try again!")
    
    if user1_won:
        print(f"{player1}, you won the game!!!")
    else:
        print(f"{player2}, won the game!!!")

    


print('''
    Options to play:
    1. With computer.
    2. With other player.
    ''')

usr_choice = int(input("Enter your choice: "))

if usr_choice == 1:
    player = input("Enter your name: ")
    vscomputer(player, board)
else:
    player1 = input("Enter first player's name: ")
    player2 = input("Enter second player's name: ")
    vsplayer(player1, player2)

# print_board(board)
