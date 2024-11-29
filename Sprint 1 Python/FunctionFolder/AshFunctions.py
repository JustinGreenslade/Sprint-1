from FunctionFolder import ReturnToMenu

def TravelClaim():
    '''
    Name: Ashton Dennis
    Desc: Allows employees to record required information for travel claims
    Date: Oct 21, 2024 - Oct 30, 2024
    '''
    # Program modules
    from os import system, name
    import datetime as dt
    
    # Program constants
    DAILY_RATE = 85
    MILEAGE_RATE_OWN = 0.17
    MILEAGE_RATE_RENT = 65
    HST_RATE = 0.15

    while True:
        # User inputs and validation
        # Despite only needing 2 validations, i'm opting to validate them all
        # I hope this isn't a problem


        print()
        print()
        print("                              Travel Claim Program")
        print()
        print("--------------------------------------------------------------------------------")
        print()
        print()
        
        while True: 
            # For the employee num, despite it saying 'num', 
            # I'm gonna make it a mix of letters and numbers
            employeeNum = input("Employee Number (XXXXX):           ").upper()
            if employeeNum == "": # If not entered
                print("\nData Entry Error - Employee number must be entered...\n")
            elif len(employeeNum) != 5: # If not exactly 5 characters
                print("\nIData Entry Error - Employee number must be 5 characters...\n")
            elif employeeNum.isalnum() == False: # If contains anything but letters and numbers
                print("\nData Entry Error - Invalid characters used (must be letters or numbers)...\n")
            else:
                break
        
        while True:
            employeeFirst = input("First name:                        ").title()
            if employeeFirst == "": # If not entered
                print("\nData Entry Error - First name must be entered...\n")
            else:
                break
        
        while True:
            employeeLast =  input("Last name:                         ").title()
            if employeeLast == "": # If not entered
                print("\nData Entry Error - Last name must be entered...\n")
            else:
                break
        
        while True:
            location = input("Trip location:                     ")
            if location == "": # If not entered
                print("\nData Entry Error - Location must be entered...\n")
            else:
                break
        
        while True:
            startDate = input("Departure Date (YYYY/MM/DD):       ")
            try:
                startDateObj = dt.datetime.strptime(startDate, "%Y/%m/%d")
            except: # If bad format
                print("\nData Entry Error - Start date must be inputted in the format YYYY/MM/DD...\n")
            else:
                break

        while True:
            endDate = input("Return Date (YYYY/MM/DD):          ")
            try:
                endDateObj = dt.datetime.strptime(endDate, "%Y/%m/%d")
            except: # If bad format
                print("\nData Entry Error - End date must be inputted in the format YYYY/MM/DD...\n")
            else:
                if startDateObj + dt.timedelta(days=7) < endDateObj: # If more than a week after departure
                    print("\nData Entry Error - End date can be no more than 7 days after the start date...\n")
                elif endDateObj < startDateObj:
                    print("\nData Entry Error - End date cannot be before departure date...\n")
                else:
                    break

        while True:
            ownOrRented = input("Own or rented car (O/R):           ").upper()
            if ownOrRented == "O":
                ownCar = True
                break
            elif ownOrRented == "R":
                ownCar = False
                break
            else: # If not O/R
                print("\nData Entry Error - Must be O/R...\n")
        
        while True:
            if ownCar:
                kmTraveled = input("KM traveled:                       ")
                try:
                    kmTraveled = float(kmTraveled)
                except: # If not a number
                    print("\nData Entry Error - KM traveled must be a number...\n")
                else:
                    if kmTraveled > 2000: # If over 2,000
                        print("\nData Entry Error - KM traveled must be no more than 2,000 KM...\n")
                    else:
                        break
            else:
                kmTraveled = 0
                break
        
        while True:
            claimType = input("Standard or executive claim (S/E): ").upper()
            if claimType == "S" or claimType == "E":
                break
            else: # If not S/E
                print("\nData Entry Error - Must be S/E...\n")

        # Calculations:

        # Assigning some constants here because i need the 
        # Start date to be defined first
        BONUS_DAYS_START = dt.datetime(startDateObj.year, 12, 15)
        BONUS_DAYS_END = dt.datetime(startDateObj.year, 12, 22)

        totalDays = (endDateObj - startDateObj).days

        perDiem = totalDays * DAILY_RATE

        if ownCar:
            mileage = MILEAGE_RATE_OWN * kmTraveled
        else:
            mileage = MILEAGE_RATE_RENT * totalDays

        bonus = 0
        if totalDays > 3:
            bonus += 100
        if kmTraveled > 1000 and ownCar:
            bonus += 0.04 * kmTraveled
        if claimType == "E":
            bonus += 45 * totalDays
        if BONUS_DAYS_START <= startDateObj <= BONUS_DAYS_END:
            bonus += 50 * totalDays

        claimAmount = perDiem + mileage + bonus
        hst = claimAmount * HST_RATE

        claimTotal = claimAmount + hst

        # Display variables
        startDateDsp = startDateObj.strftime("%b %d, %Y")
        endDateDsp = endDateObj.strftime("%b %d, %Y")
        ownOrRentedDsp = "Own Car" if ownOrRented == "O" else "Rented Car"
        claimTypeDsp = "Standard" if claimType == "S" else "Executive"
        kmTraveledDsp = f"{kmTraveled:,.02f}"
        totalDaysDsp = f"{totalDays} days"
        perDiemDsp = f"${perDiem:,.02f}"
        mileageDsp = f"${perDiem:,.02f}"
        bonusDsp = f"${bonus:,.02f}"
        claimAmountDsp = f"${claimAmount:,.02f}"
        hstDsp = f"${hst:,.02f}"
        claimTotalDsp = f"${claimTotal:,.02f}"

        # Outputs
        system("cls" if name == "nt" else "clear")
        print( "Inputs: ")
        print(f"    Employee Number:   {employeeNum}")
        print(f"    First Name:        {employeeFirst}")
        print(f"    Last Name:         {employeeLast}")
        print(f"    Trip Location:     {location}")
        print(f"    Departure Date:    {startDateDsp}")
        print(f"    Return Date:       {endDateDsp}")
        print(f"    Own or Rented Car: {ownOrRentedDsp}")
        if ownCar:
            print(f"    KM Traveled:       {kmTraveledDsp}")
        print(f"    Claim Type:        {claimTypeDsp}")
        print()
        print( "Calculations:")
        print(f"    Length of Trip: {totalDaysDsp:>9s}")
        print(f"    Per Diem Amount:{perDiemDsp:>9s}")
        print(f"    Mileage:        {mileageDsp:>9s}")
        print(f"    Bonus:          {bonusDsp:>9s}")
        print(f"    Claim Amount:   {claimAmountDsp:>9s}")
        print(f"    HST:            {hstDsp:>9s}")
        print(f"    Claim Total:    {claimTotalDsp:>9s}")
        print()

        # Ask if user would like to do it again. if not, return to main menu
        while True:
            continuer = input("Would you like to process another claim? (Y/N): ").upper()
            if continuer == "Y":
                system("cls" if name == "nt" else "clear")
                break
            elif continuer == "N":
                ReturnToMenu.ReturnToMenu()
                return
            else:
                print("\nData Entry Error - Must be Y/N...\n")

