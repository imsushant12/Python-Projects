from datetime import date
import os

def result(marks, user):
    # calculating grades:
    percentage = float(marks)*(100.0/500.0)
    if(percentage > 80.0):
        print("Grade: Excellent!")
        print(f"{user}, you scored: ", str(marks),
              " out of 5 and your percentage is: ", str(percentage), "%")

# Java Test:
def java(user):
    print("Welcome to the Java test")
    print("------------------------")

    questions = [
        {
            "Question - ": "Which of the following option leads to the portability and security of Java?",
            "1.  ": "Bytecode is executed by JVM",
            "2.  ": "The applet makes the Java code secure and portable",
            "3.  ": "Use of exception handling",
            "4.  ": "Dynamic binding between objects"
        },
        {
            "Question - ": "Which of the following is not a Java features?",
            "1.  ": "Dynamic",
            "2.  ": "Architecture Neutral",
            "3.  ": "Use of pointers",
            "4.  ": "Object-oriented"
        },
        {
            "Question - ": "The '\u0021' article referred to as a",
            "1.  ": "Line feed",
            "2.  ": "Unicode escape sequence",
            "3.  ": "Hexadecimal",
            "4.  ": "Octal escape"
        },
        {
            "Question - ": "_____ is used to find and fix bugs in the Java programs.",
            "1.  ": "JVM",
            "2.  ": "JRE",
            "3.  ": "JDK",
            "4.  ": "JDB"
        },
        {
            "Question - ": "What does the expression float a = 35 / 0 return?",
            "1.  ": "Infinity",
            "2.  ": "0",
            "3.  ": "Not a Number",
            "4.  ": "Run time exception"
        }
    ]
    answers = [1, 3, 2, 4, 1]
    marks = 0
    # displaying questions:
    for i in range(5):
        for key, value in questions[i].items():
            print("\n" , key, value)
        answer = int(input("Your answer: "))
        # Checking answers
        if(answer == answers[i]):
            marks = marks + 1
    
    result(marks, user)


# ----------------------------------------------------------------------------------
# Python Test:
def python(user):
    print("Welcome to the Python test")
    print("--------------------------")
    questions = [
        {
            "Question - ": "What is the maximum possible length of an identifier?",
            "1.  ": "16",
            "2.  ": "32",
            "3.  ": "64",
            "4.  ": "None of these"
        },
        {
            "Question - ": "Who developed the Python language?",
            "1.  ": "Zim Den",
            "2.  ": "Guido van Rossum",
            "3.  ": "Niene Stom",
            "4.  ": "Wick van Rossum"
        },
        {
            "Question - ": "In which year was the Python language developed?",
            "1.  ": "1995",
            "2.  ": "1972",
            "3.  ": "1981",
            "4.  ": "1989"
        },
        {
            "Question - ": "In which language is Python written?",
            "1.  ": "C",
            "2.  ": "PHP",
            "3.  ": "C++",
            "4.  ": "None of these"
        },
        {
            "Question - ": "Which one of the following is the correct extension of the Python file?",
            "1.  ": ".p",
            "2.  ": ".python",
            "3.  ": ".py",
            "4.  ": "None of these"
        }
    ]
    answers = [4, 2, 4, 1, 3]
    marks = 0
    # displaying questions:
    for i in range(5):
        for key, value in questions[i].items():
            print("\n" , key, value)
        answer = int(input("Your answer: "))
        # Checking answers
        if(answer == answers[i]):
            marks = marks + 1

    result(marks, user)


# ----------------------------------------------------------------------------------
# JavaScript Test:
def javascript(user):
    print("Welcome to the JavaScript test")
    print("------------------------------")
    questions = [
        {
            "Question - ": "Which type of JavaScript language is ___",
            "1.  ": "Object-Oriented",
            "2.  ": "Object-Based",
            "3.  ": "Assembly-language",
            "4.  ": "High-level"
        },
        {
            "Question - ": "Which one of the following also known as Conditional Expression:",
            "1.  ": "Alternative to if-else",
            "2.  ": "Switch statement",
            "3.  ": "If-then-else statement",
            "4.  ": "immediate if"
        },
        {
            "Question - ": "In JavaScript, what is a block of statement?",
            "1.  ": "Conditional block",
            "2.  ": "block that combines a number of statements into a single compound statement",
            "3.  ": "both conditional block and a single statement",
            "4.  ": "block that contains a single statement"
        },
        {
            "Question - ": "When interpreter encounters an empty statements, what it will do:",
            "1.  ": "Shows a warning",
            "2.  ": "Prompts to complete the statement",
            "3.  ": "Throws an error",
            "4.  ": "Ignores the statements"
        },
        {
            "Question - ": "The function and var are known as:",
            "1.  ": "Keywords",
            "2.  ": "Data types",
            "3.  ": "Declaration statements",
            "4.  ": "Prototypes"
        }
    ]
    answers = [2, 4, 2, 4, 3]
    marks = 0
    # displaying questions:
    for i in range(5):
        for key, value in questions[i].items():
            print("\n" , key, value)
        answer = int(input("Your answer: "))
        # Checking answers
        if(answer == answers[i]):
            marks = marks + 1

    result(marks, user)


# ----------------------------------------------------------------------------------
# Quiz game:
def quiz(user):
    print("-----------------------")
    print(f"Welcome {user}!")
    print("-----------------------")
    print('''
    Welcome to the Quiz, PLease select your language:
        1. Python
        2. Java
        3. JavaScript
    ''')

    option = int(input("Enter your choice: "))

    if option == 1:
        python(user)

    elif option == 2:
        java(user)

    elif option == 3:
        javascript(user)

    else:
        print("Invalid choice!")
        quiz(user)


# ----------------------------------------------------------------------------------
# Registration:
def register():
    print("\nWelcome! Please register yourself to use the portal.")
    print("----------------------------------------------------")
    name = input("Enter your name: ")
    enroll = input("Enter your enrollment-number: ")
    college = input("Enter your college: ")
    password = input("Enter your password: ")

    # Writing user's data into a file.
    file = open(f"{enroll}.txt", 'w')
    file.write(enroll + "\n")
    file.write(password + "\n")
    file.write(name + "\n")
    file.write(college + "\n")
    file.close()

    print("Your are now registered!")
    current_choice = input("Do you want to give test? (yes) or (no): ")

    if(current_choice.lower() == "yes"):
        login()
    else:
        exit()


# ----------------------------------------------------------------------------------
# Login:
def login():
    print("\nPlease enter your credentials to give the test.")
    print("-----------------------------------------------")
    user = input("Enter your enrollment-number: ")
    user_pwd = input("Enter your password: ")

    # checking if the user is registered or not:
    if os.path.exists(f"{user}.txt"):
        # Reading user's dat from file.
        file = open(f"{user}.txt", 'r')
        enrollment = file.readline().strip()
        password = file.readline().strip()
        name = file.readline().strip()
        file.close()

        # Checking the credentials:
        if(user == enrollment and user_pwd == password):
            print("\nSuccessfullly logged in!")
            # Redirecting to test:
            quiz(name)

        else:
            print("\nWrong credentials, please try again!")
            current_choice = input("Login in again? (yes) or (no): ")
            if(current_choice.lower() == "yes"):
                login()
            else:
                exit()

    else:
        print("Your are not registered!")
        current_choice = input("Do you want to register? (yes) or (no): ")

        if(current_choice.lower() == "yes"):
            register()
        else:
            exit()


if __name__ == "__main__":
    print("===============================")
    print("||  SKILLTESTER : Quiz Game  ||")
    print("===============================")
    print("Todays date: ", date.today())

    print('''
    Welcome to the Quiz Portal
        1. Register Yourself
        2. Start Quiz
        3. Exit
    ''')

    option = int(input("Enter your choice: "))

    if option == 1:
        register()

    elif option == 2:
        login()

    else:
        exit(0)
