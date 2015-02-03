# Jamie Hilton
# 09/12/14
# Lists R+R
in_use = True
name1 = input("Please enter the Name of the First student: ")
name2 = input("Please enter the Name of the Second student: ")
name3 = input("Please enter the Name of the Third student: ")
name4 = input("Please enter the Name of the Fourth student: ")
name5 = input("Please enter the Name of the Fith student: ")
name6 = input("Please enter the Name of the Sixth student: ")
name7 = input("Please enter the Name of the Seventh student: ")
name8 = input("Please enter the Name of the Eighth student: ")
while in_use == True:
    print("1. {0}".format(name1))
    print("2. {0}".format(name2))   
    print("3. {0}".format(name3))
    print("4. {0}".format(name4))
    print("5. {0}".format(name5))
    print("6. {0}".format(name6))
    print("7. {0}".format(name7))
    print("8. {0}".format(name8))
    print("0. Quit Program")



    choice = int(input("Please select a student to edit: "))
    if choice == 1:
        name1 = input("Please enter their new name: ")
    elif choice == 2:
        name2 = input("Please enter their new name: ")
    elif choice == 3:
        name3 = input("Please enter their new name: ")
    elif choice == 4:
        name4 = input("Please enter their new name: ")
    elif choice == 5:
        name5 = input("Please enter their new name: ")
    elif choice == 6:
        name6 = input("Please enter their new name: ")
    elif choice == 7:
        name7 = input("Please enter their new name: ")
    elif choice == 8:
        name8 = input("Please enter their new name: ")
    elif choice == 0:
        in_use = False
    else:
        print("That is not a valid option")
