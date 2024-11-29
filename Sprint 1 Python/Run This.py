'''
Desc: The main menu program, the program the user should be running. Allows user to choose an option and have that function be used.
Name: Entire project by Justin Greenslade, Joseph Gallant and Ashton Dennis. Main Menu program by Ashton Dennis
Date: Oct 21, 2024 - Oct 30, 2024
Ver: 1.7
Note: You may notice the use of sleep() and system("cls" if name == "nt" else "clear"). while i know it isn't in scope i thought i'd include them for a better viewing experience
'''
# Program modules
from FunctionFolder import AshFunctions, JosephFunctions, JustinFunctions
from time import sleep
from os import system, name

system("cls" if name == "nt" else "clear")
while True:
    # Display menu and take user choice
    print("Midterm Sprint - Main Menu\n")
    print("1. Complete a travel claim.")
    print("2. Fun interview question.")
    print("3. Cool stuff with strings and dates.")
    print("4. A little bit of everything.")
    print("5. Something old, something new.")
    print("6. Quit.\n")

    while True:
        userChoice = input("   Enter choice (1-6): ")
        match userChoice:
            case "1":
                system("cls" if name == "nt" else "clear")
                print("Opening: \"Complete a travel claim...\"")
                sleep(1.5)
                system("cls" if name == "nt" else "clear")
                AshFunctions.TravelClaim()
                sleep(1)
                system("cls" if name == "nt" else "clear")
                break
            case "2":
                system("cls" if name == "nt" else "clear")
                print("Opening: \"Fun interview question...\"")
                sleep(1.5)
                system("cls" if name == "nt" else "clear")
                JosephFunctions.FizzBuzz()
                sleep(1)
                system("cls" if name == "nt" else "clear")
                break
            case "3":
                system("cls" if name == "nt" else "clear")
                print("Opening: \"Cool stuff with strings and dates...\"")
                sleep(1.5)
                system("cls" if name == "nt" else "clear")
                JustinFunctions.CoolStuffWithStringsAndDates()
                sleep(1)
                system("cls" if name == "nt" else "clear")
                break
            case "4":
                system("cls" if name == "nt" else "clear")
                print("Opening: \"A little bit of everything...\"")
                sleep(1.5)
                system("cls" if name == "nt" else "clear")
                JosephFunctions.XYZCompanyMaintenance()
                sleep(1)
                system("cls" if name == "nt" else "clear")
                break
            case "5":
                system("cls" if name == "nt" else "clear")
                print("Opening: \"Something old, something new...\"")
                sleep(1.5)
                system("cls" if name == "nt" else "clear")
                JustinFunctions.List()
                sleep(1)
                system("cls" if name == "nt" else "clear")
                break
            case "6":
                system("cls" if name == "nt" else "clear")
                print("Thank you for using our program!")
                sleep(1)
                exit()
            case _:
                system("cls" if name == "nt" else "clear")
                print("Data Entry Error - Must be a number from 1-6...")
                sleep(3)
                system("cls" if name == "nt" else "clear")
                break
