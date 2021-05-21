import os

print("\t\t\t\t\t\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\t\t\t\t\t\t\t\t ||  THE PRETTY FOLDER  ||")
print("\t\t\t\t\t\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

path = input("Enter the complete path of the folder : ")
filename = input("Enter that file-name that you don't want to change :  ")
extension = input("Enter the extension of file which is to be numbered serially : ")

# getting the actual path of the folder.
os.chdir(path)
# getting all the files and directories in list.
filesList = os.listdir(path)
# a variable for numbering the files.
numbering = 1

for i in filesList:
    # splitting the files as name and extension.
    # noChnage will keep extensions.
    noChange = os.path.splitext(i)

    if(noChange[1] == extension):
        os.rename(i , f"{numbering}.jpg")
        numbering += 1

    elif(noChange[0] != filename):
        new = str(i).capitalize()
        os.rename(i , new)
