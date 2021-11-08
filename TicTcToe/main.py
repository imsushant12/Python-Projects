'''
from random import choice

print("\t\t\t\t\t\t\t ===============")
print("\t\t\t\t\t\t\t | Tic Tac Toe |")
print("\t\t\t\t\t\t\t ===============\n")


board = [
    [" 1 ", " 2 ", " 3 "],
    [" 4 ", " 5 ", " 6 "],
    [" 7 ", " 8 ", " 9 "],
]


def coordinates(user_input):
    rows = int(user_input / 3)
    # will handle the condition of first row:
    columns = user_input
    # will handle the condition for rest of the rows:
    if columns > 2:
        columns = int(columns % 3)

    return (rows, columns)


def add_to_board(coordinate, board):
    board[coordinate[0]][coordinate[1]] = "X"

def check(user_input, board):
    user_input = user_input - 1
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
            # Defining the coordinates of the input:
            coordinate = coordinates(user_input)
            add_to_board(coordinate, board)
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


print("""
    Options to play:
    1. With computer.
    2. With other player.
    """)

usr_choice = int(input("Enter your choice: "))

if usr_choice == 1:
    player = input("Enter your name: ")
    print_board(board)
    vscomputer(player, board)
else:
    player1 = input("Enter first player's name: ")
    player2 = input("Enter second player's name: ")
    vsplayer(player1, player2)

'''

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

user = True  # when true it refers to x, otherwise o
turns = 0


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing")
        return True
    else:
        return False


def check_input(user_input):
    # check if its a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # check if its 1 - 9
    if not bounds(user_input):
        return False

    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This is number is out of bounds")
        return False
    else:
        return True


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False


def check_diag(user, board):
    # top left to bottom right
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


print("\t\t\t\t\t ===============")
print("\t\t\t\t\t | Tic Tac Toe |")
print("\t\t\t\t\t ===============\n")

print("Choose your position according to the number system!")
print('''
---------------
| 1 || 2 || 3 |
---------------
| 4 || 5 || 6 |
---------------
| 7 || 8 || 9 | 
---------------
''')

while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input(
        "Please enter a position 1 through 9 or enter \"q\" to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again!")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again!")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    turns += 1
    if turns == 9:
        print("Tie!")
    user = not user
