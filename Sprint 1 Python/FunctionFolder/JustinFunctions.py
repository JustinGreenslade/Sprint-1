from FunctionFolder import ReturnToMenu

def CoolStuffWithStringsAndDates():

    # Description: a simple Python program that does cool stuff with strings and dates based on employee information
    # Author: Justin Greenslade
    # Date(s): Oct 21-31, 2024


    # Define required libraries.
    import datetime




    # Define program constants.
    ALLOWED_NAME_CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVTXYZ abcdefghijklmnopqrstuvwxyz-")
    ALLOWED_NUMBER_CHARACTERS = set("1234567890")
    CURRENT_DATE = datetime.datetime.now()
    RETIREMENT_AGE = 65
    # Define program functions.



    # Main program starts here.
    while True:

        print()
        print()
        print("                       Cool Stuff With Strings and Dates")
        print()
        print("--------------------------------------------------------------------------------")
        print()
        print()
        
        # Gather user inputs.
        # Gets Employee first name.
        while True:
            firstName = input("Enter the Employee first name (To end program type END): ").title()
            print()
            if firstName == "":
                print()
                print("Data entry error - first name must be entered...")
                print()
            elif set(firstName).issubset(ALLOWED_NAME_CHARACTERS) == False:
                print()
                print("Data entry error - first name must be valid characters...")
                print()
            else:
                break

        # If Employee first name entered "END" it will end the program.
        if firstName.upper() == "END":
            ReturnToMenu.ReturnToMenu()
            return

        # Gets Employee last name.
        while True:
            lastName = input("Enter the Employee last name: ").title()
            print()
            if lastName == "":
                print()
                print("Data entry error - last name must be entered...")
                print()
            elif set(lastName).issubset(ALLOWED_NAME_CHARACTERS) == False:
                print()
                print("Data entry error - last name must be valid characters...")
                print()
            else:
                break

        # Gets Employee phone number.
        while True: 
            phoneNumber = input("Enter the Employee phone number (0000000000): ")
            print()
            if phoneNumber == "":
                print()
                print("Data entry error - phone number must be entered...")
                print()
            elif set(phoneNumber).issubset(ALLOWED_NUMBER_CHARACTERS) == False:
                print()
                print("Data entry error - phone number must be valid characters...")
                print()
            elif len(phoneNumber) != 10:
                print()
                print("Data entry error - phone number must be 10 characters...")
                print()
            else:
                break

        # Gets Employee start date
        while True:
            try:
                startDate = input("Enter the Employee start date (YYYY/MM/DD): ")
                print()
                startDate = datetime.datetime.strptime(startDate, "%Y/%m/%d")
            except:
                print()
                print("   Data Entry Error - Start date is invalid - use YYYY/MM/DD format ...")
                print()
            else:
                break

        while True:
            try:
                birthDate = input("Enter the Employee Birth date (YYYY/MM/DD): ")
                print()
                birthDate = datetime.datetime.strptime(birthDate, "%Y/%m/%d")
            except:
                print()
                print("   Data Entry Error - Birth date is invalid - use YYYY/MM/DD format ...")
                print()
            else:
                break

        # Generate Employee ID
        employeeID = f"{lastName[:3].upper()}{firstName[:2].upper()}{CURRENT_DATE.year}"

        # Create Username
        userName = f"{firstName[:1].upper()}.{lastName.title()}{birthDate.year}"

        # Calculate duration of employment
        employmentDuration = CURRENT_DATE - startDate
        yearsWorked = employmentDuration.days // 365
        remainingDays = employmentDuration.days % 365
        daysWorked = 0

        # Start from the beginning of the employment period to the current date
        currentYear = CURRENT_DATE.year
        startYear = startDate.year

        # Loop through each year to count days accurately
        for year in range(startYear, currentYear + 1):
            if year == startYear:

                # For the start year, count from the start date to the end of that year
                endOfStartYear = datetime.datetime(year, 12, 31)
                daysWorked += (endOfStartYear - startDate).days + 1  # Include the start date
            elif year == currentYear:

                # For the current year, count from the beginning of the year to today
                daysWorked += (CURRENT_DATE - datetime.datetime(year, 1, 1)).days + 1  # Include today
            else:

                # For full years in between, check if it's a leap year
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    daysWorked += 366  # Leap year
                else:
                    daysWorked += 365  # Regular year

        # Calculate time until retirement
        age = CURRENT_DATE.year - birthDate.year
        if (CURRENT_DATE.month, CURRENT_DATE.day) < (birthDate.month, birthDate.day):
            age -= 1
        retirement = RETIREMENT_AGE - age

        # Calculate days until next birthday
        nextBirthday = datetime.datetime(CURRENT_DATE.year, birthDate.month, birthDate.day)
        if nextBirthday < CURRENT_DATE:
            nextBirthday = datetime.datetime(CURRENT_DATE.year + 1, birthDate.month, birthDate.day)
        daysUntilBirthday = (nextBirthday - CURRENT_DATE).days

        # Generate simple password
        password = f"{firstName[0].upper()}{lastName.lower()}{CURRENT_DATE.year}"


        print(f"----------------------------------------------")
        print(f"            Employee Information")
        print(f"----------------------------------------------")
        print()
        print(f"Employee Id:               {employeeID}")
        print()
        print(f"Username:                  {userName}")
        print(f"Password:                  {password}")
        print()
        print(f"Days until birthday:       {daysUntilBirthday} day(s)")
        print(f"Worked at company for:     {yearsWorked} year(s), {daysWorked} day(s)")
        print(f"How long until retirement: {retirement} year(s)")

def List():

    # Description: A list program to add items view them or deleted them and it saves them in a json file
    # Author: Justin Greenslade
    # Date(s): Oct 21-31, 2024

    # Imports the json Module.
    import json
    from os import system, name
    from time import sleep
     

    # Defines the file name where our list will be saved.
    FILE_NAME = "MyList.json"


    # Trys to load the data.
    def LoadList():
        try:
            # Trys to open the file (with "r" is to open the file in read mode) as a file
            # using "as file" ensures proper handling of the file
            # When "with" in front of it is used it will automatically close the file when your done with it.
            with open(FILE_NAME, "r") as file:
                # If file is found it will load the data and return it as a python list
                return json.load(file)
            # If the file does not exist the it gets returned as empty ( [] )
        except FileNotFoundError:
            return []

    # Trys to save the data.
    def SaveList(itemList):
        # Opens the file in write mode ( "w" )
        with open(FILE_NAME, "w") as file:
            # This stores data and converts it to a json format and will write it to the file.
            # The indent = 4 allows for readability. allows indentation and linebreaks.
            json.dump(itemList, file, indent=4) 

    # Main loop of the program
    # The "Main" function initalizes the program by loading any existing list items
    # and enters a loop where it displays a menu and processes the user input.
    def Main():
        # Loads existing items.
        itemList = LoadList()

        while True:
            # Displays the menu and gets user to choose the input.
            system("cls" if name == "nt" else "clear")
            print(f"    Menu")
            print(f"--------------")
            print("1. Add item")
            print("2. View items")
            print("3. Delete item")
            print("4. Exit")
            print()
            choice = input("Choose an option: ")

            # Menu Options 
            # Adding an item
            system("cls" if name == "nt" else "clear")
            if choice == "1":
                # If the user selects 1 they will enter an item they want to add to the list.
                item = input("Enter the item to add: ")
                # Adds the item to the list using the "append"
                itemList.append(item)
                print(f"Successfully added {item} to list")
                # Calls for the savelist function to save the updated itemlist.
                SaveList(itemList)
                sleep(2)

            # Viewing the items
            # If the user selects 2 they will view the items in list if any.
            elif choice == "2":
                # Checks to see if itemlist is empty
                if itemList:
                    # Uses the enumerate function to loop though the itemlist and adds a counter to each item in the list.
                    # Start ensures it will start at 1 and count upwards
                    print()
                    print(f"   List items")
                    print(f"----------------")
                    for number, item in enumerate(itemList, start=1):
                        # Inside the loop each item will be printed with a number counting each item on the list.
                        print(f"{number}. {item}")
                    input("\nPress ENTER to continue ")
                else:
                    system("cls" if name == "nt" else "clear")
                    print("There are no items in your list!")
                    sleep(2)

            # Deleting an item
            # If the user selects "3" then will be prompted the numbered items to remove one from the list.
            elif choice == "3":
                # Displays list to make chose of what to delete
                if itemList:
                    # Uses the enumerate function to loop though the itemlist and adds a counter to each item in the list.
                    # Start ensures it will start at 1 and count upwards
                    print()
                    print(f"   List items")
                    print(f"----------------")
                    for number, item in enumerate(itemList, start=1):
                        # Inside the loop each item will be printed with a number counting each item on the list.
                        print(f"{number}. {item}")
                    print()

                    # Ensure number is entered as an integer
                    while True:
                        try:
                            # The - 1 accounts for the zero-based index of python 
                            number = int(input("Enter the number of the item to delete it: ")) - 1
                            # The "pop" method is called on the itemlist to target the chosen number removing it and storing it as removedItem.
                            if 0 <= number < len(itemList):  # Check if the number is valid
                                removedItem = itemList.pop(number)
                                # Updates and saves the list.
                                SaveList(itemList)
                                print(f"Successfully deleted {removedItem} from list")
                                sleep(2)
                                break
                            else:
                                print("Invalid item number.")
                                sleep(2)
                        except ValueError:
                            print("Please enter a valid number.")
                            sleep(2)
                else:
                    system("cls" if name == "nt" else "clear")
                    print("There's nothing to remove!")
                    sleep(2)

            # Exiting the program
            elif choice == "4":
                ReturnToMenu.ReturnToMenu()
                return

    Main()  # Call the main function to start the program