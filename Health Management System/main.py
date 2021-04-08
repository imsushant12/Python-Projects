print("\t\t\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t\t\t\t\t\t ||   THE HEALTH MANAGER  ||")
print("\t\t\t\t\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\tHi! Save your DIET & EXERCISE here.\n")

while(1):
    answer = int(input("Enter  1:View Saved Data\t\t\t2:Add Data\t\t\t3:EXIT\n"))

    if answer ==3:
        exit(0)

    name = int(input("Press 1 for Sushant \t 2 for Aman \t 3 for Aditya\n"))
    type = int(input("Press 1 for EXERCISE \t 2 for DIET\n"))

    def getdate():
        '''To get the current date and time at time of entry'''
        import datetime
        return (str(datetime.datetime.now()))

    #READING FROM THE FILE
    if answer == 1:
        # If the user is SUSHANT
        if name == 1:
            if type == 1:
                try:
                    f = open("sushant_exer.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            elif type == 2:
                try:
                    f = open("sushant_diet.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            else:
                print("\nWRONG INPUT!")


        # If the user is AMAN
        elif name == 2:
            if type == 1:
                try:
                    f = open("aman_exer.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            elif type == 2:
                try:
                    f = open("aman_diet.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            else:
                print("\nWRONG INPUT!")


        # If the user is ADITYA
        elif name == 3:
            if type == 1:
                try:
                    f = open("aditya_exer.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            elif type == 2:
                try:
                    f = open("aditya_diet.txt", "rt")
                    print("\nDetails :")
                    print(f.read())
                    f.close()
                except:
                    print("Details not found")

            else:
                print("\nWRONG INPUT!")


    #WRITING TO THE FILE
    if answer == 2:
        # If the user is SUSHANT
        if name == 1:
            if type == 1:
                f = open("sushant_exer.txt","at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter exercise you have done : "))
                f.write("\n")
                f.close()

            elif type == 2:
                f = open("sushant_diet.txt","at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter diet you have taken : "))
                f.write("\n")
                f.close()

            else:
                print("\nWRONG INPUT!")


        # If the user is AMAN
        elif name == 2:
            if type == 1:
                f = open("aman_exer.txt","at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter exercise you have done : "))
                f.write("\n")
                f.close()

            elif type == 2:
                f = open("aman_diet.txt","at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter diet you have taken : "))
                f.write("\n")
                f.close()

            else:
                print("\nWRONG INPUT!")


        # If the user is ADITYA
        elif name == 3:
            if type == 1:
                f = open("aditya_exer.txt", "at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter exercise you have done : "))
                f.write("\n")
                f.close()

            elif type == 2:
                f = open("aditya_diet.txt", "at")
                f.write("[ "+getdate()+" ] ")
                f.write(input("Enter diet you have taken : "))
                f.write("\n")
                f.close()

            else:
                print("\nWRONG INPUT!")