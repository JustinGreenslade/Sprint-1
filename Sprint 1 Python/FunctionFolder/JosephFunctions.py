from FunctionFolder import ReturnToMenu

def FizzBuzz():
    # Desc.: Fun Interview Question - Fizz Buzz Program - It will display Fizz, Buzz or FizzBuzz, depending on the conditions.
    # Author: Joseph Gallant
    # Dates: Oct. 21 2024 - Oct. 30 2024

    # This function displays a number, the message "Fizz", "Buzz", or "FizzBuzz", depending on the conditions.

    # Assign the constants
    MIN_NUM = 1
    MAX_NUM = 100

    # Print the header
    print()
    print()
    print("               Fizz, Buzz, and FizzBuzz - Fun Interview Question")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"FizzBuzz messages for the numbers between {MIN_NUM} and {MAX_NUM}:")
    print()

    # Execute for a range of numbers (1-100)
    for number in range(MIN_NUM, MAX_NUM + 1):

        message = ""
        if number % 5 == 0:
            message += "Fizz"
        
        if number % 8 == 0:
            message += "Buzz"

        if message == "":
            print(number)

        else:
            print(message)

    # Print the footer
    print()
    print()
    print(f"********************************************************************************")
    print(f"*              Thank you for using our program. Have a nice day!               *")
    print(f"********************************************************************************")
    print()

    input("\nPress ENTER to return to the Main Menu")
    ReturnToMenu.ReturnToMenu()
    return

def XYZCompanyMaintenance():
    # Desc.: A Little Bit of Everything - XYZ Company maintenance schedule program.
    # Author: Joseph Gallant
    # Dates: Oct. 21 2024 - Oct. 30 2024

    import datetime

    # Assign the constants
    TODAY_DATE = datetime.datetime.now()
    CLEAN_INTERV_DAYS = 10
    TUBE_FLUIDS_INTERV_DAYS = 21
    INSPECT_INTERV_MONTHS = 6
    SALVAGE_RATE = 0.10
    AMORTIZATION_MONTHS = 180 # 15 years

    todayDateDsp = datetime.datetime.strftime(TODAY_DATE, "%B %d, %Y") # 18 characters long (max)

    # Print the header with today's date
    print()
    print()
    print(f"                                   XYZ Company                                  ")
    print()
    print(f"                                                              {todayDateDsp:>18s}")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"                        Maintenance Schedule - Data Entry                       ")
    print()
    print()

    # Validation for the cost
    while True:
        cost = input("Enter the part cost: ")

        if cost == "":
            print()
            print("Data Entry Error - Part cost is required...")
            print()
        else:
            try:
                cost = float(cost)

            except:
                print()
                print("Data Entry Error - Part cost must be a number...")
                print()
            else:

                if cost < 0:
                    print()
                    print("Data Entry Error - Part cost must be a positive number...")
                    print()

                break

    # Validation for the purchaseDate
    while True:
        purchaseDate = input("Enter the date of purchase (YYYY/MM/DD): ")

        if purchaseDate == "":
            print()
            print("Data Entry Error - Purchase date is required...")
            print()
        else:

            try:
                purchaseDate = datetime.datetime.strptime(purchaseDate, "%Y/%m/%d")

            except:
                print()
                print("Data Entry Error - Invalid purchase date format...")
                print()
            else:
                break

    # Dates for the scheduled maintenance (part 1)
    baseCleaningDate = purchaseDate + datetime.timedelta(CLEAN_INTERV_DAYS)
    tubeFluidsChkDate = purchaseDate + datetime.timedelta(TUBE_FLUIDS_INTERV_DAYS)

    inspectionMonth = purchaseDate.month + INSPECT_INTERV_MONTHS
    inspectionYear = purchaseDate.year

    # If the inspection month falls on the next year, adjust the month to roll over and increment the year value by one.
    if purchaseDate.month + INSPECT_INTERV_MONTHS >= 12:
        inspectionMonth = purchaseDate.month + INSPECT_INTERV_MONTHS - 12
        inspectionYear += 1

    # Dates for the scheduled maintenance (part 2)
    inspectionDate = datetime.datetime(inspectionYear, inspectionMonth, purchaseDate.day)
    
    # Calculations
    salvageValue = cost * SALVAGE_RATE
    totalCost = cost - salvageValue
    amortization = totalCost / AMORTIZATION_MONTHS

    # Formatting section
    costDsp = "${:,.2f}".format(cost) # Up to $9,999,999.99 (13 characters)
    salvageValueDsp = "${:,.2f}".format(salvageValue) # Up to $999,999.99 (11 characters)
    salvageRateDsp = "{:.2%}".format(SALVAGE_RATE)
    totalCostDsp = "${:,.2f}".format(totalCost) # Up to $9,999,999.99 (13 characters)

    purchaseDateDsp = datetime.datetime.strftime(purchaseDate, "%B %d, %Y") # 18 characters long (max)
    baseCleaningDateDsp = datetime.datetime.strftime(baseCleaningDate, "%B %d, %Y") # 18 characters long (max)
    tubeFluidsChkDateDsp = datetime.datetime.strftime(tubeFluidsChkDate, "%B %d, %Y") # 18 characters long (max)

    inspectionDateDsp = datetime.datetime.strftime(inspectionDate, "%B %d, %Y") # 18 characters long (max)

    amortizationDsp = "${:,.2f}".format(amortization)

    # Display all the input values and calculated values
    print()
    print()
    print(f"                       XYZ Company - Maintenance Schedule")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print()
    print(f"Equipment Information:")
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"Cost:          {costDsp:>13s}         Purchase Date:           {purchaseDateDsp:>18s}")
    print(f"Salvage Value:   {salvageValueDsp:>11s}         ({salvageRateDsp:>6s} of the cost)")
    print(f"               -------------")
    print(f"Total cost:    {totalCostDsp:>13s}")
    print()
    print()
    print(f"Maintenance Schedule")
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"                                     Basic Cleaning Due Date: {baseCleaningDateDsp:>18s}")
    print(f"                                     Tube/Fluid Check Date:   {tubeFluidsChkDateDsp:>18s}")    
    print(f"                                     Inspection Due Date:     {inspectionDateDsp:>18s}")
    print()
    print()
    print(f"Amortization Cost")
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"Duration in Months: {AMORTIZATION_MONTHS:>3d}              Monthly Amortization:            {amortizationDsp:>10s}")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print()

    while True:
        contProgram = input("Would you like to select a financing plan (Y/N)? ").upper()

        if contProgram != "Y" and contProgram != "N":
            print()
            print("Data Entry Error - Value (Y/N) required...")
            print()
        else:
            if contProgram == "Y":
                FinancingPlan(cost)
            else:
                break

    # Print the footer
    print()
    print()
    print(f"********************************************************************************")
    print(f"*              Thank you for using our program. Have a nice day!               *")
    print(f"********************************************************************************")
    print()

    # Quit to menu
    input("\nPress ENTER to return to the Main Menu")
    ReturnToMenu.ReturnToMenu()
    return


def FinancingPlan(cost):

    # Print the header
    print()
    print()
    print(f"                                   XYZ Company                                  ")
    print()
    print(f"--------------------------------------------------------------------------------")
    print()
    print(f"                         Repayment Schedule - Data Entry                        ")
    print()
    print()

    # Validate the number of years for amortization
    while True:

        amortizationYears = input("Enter the number of years for the payment plan (0.5 increment accepted): ")

        if amortizationYears == "":
            print()
            print("Data Entry Error - Number of years must be entered...")
            print()
        else:

            try:
                amortizationYears = float(amortizationYears)

            except:
                print()
                print("Data Entry Error - Number of years must be a number...")
                print()
            else:

                if amortizationYears < 0.5:
                    print()
                    print("Data Entry Error - Number of years must be 0.5 or above...")
                    print()

                # Make sure the number is input as a whole number of 0.5 decimal value
                elif amortizationYears % 0.5 != 0:
                    print()
                    print("Data Entry Error - Number of years must be entered as increments of 0.5 (6 months)...")
                    print()
                else:

                    break
        
    amortizationMonths = int(amortizationYears * 12)

    while True:

        financingRate = input("Enter the interest rate (##.##): ")

        if financingRate == "":
            print()
            print("Data Entry Error - Interest rate must be entered...")
            print()
        else:

            try:
                financingRate = float(financingRate)
            
            except:
                print()
                print("Data Entry Error - Interest rate must be a number...")
                print()
            else:

                if financingRate <= 0:
                    print()
                    print("Data Entry Error - Interest rate must be over 0%...")
                    print()

                else:

                    # Convert the whole number as a percentage value
                    financingRate /= 100

                    break

    # Print the result

    print()
    print()
    print(f"Cost to Finance")
    print(f"--------------------------------------------------------------------------------")
    print()
    print()

    # Financing rate and repayment schedule
    rate = financingRate / 12
    payment = (rate * cost) / (1 - (1 + rate)**-amortizationMonths)
    interests = (payment * amortizationMonths) - cost
    finalCost = cost + interests

    costDsp = "${:,.2f}".format(cost)
    paymentDsp = "${:,.2f}".format(payment)
    interestsDsp = "${:,.2f}".format(interests)
    finalCostDsp = "${:,.2f}".format(finalCost)

    print()
    print(f"Original Cost:              {costDsp:>13s}")
    print(f"Cost to Finance:            {interestsDsp:>13s}")
    print(f"                           --------------")
    print(f"Total Cost:                {finalCostDsp:>14s}")
    print()
    print()
    print(f"Your monthly payment to finance the equipment at a rate of {financingRate:.2%} will be {paymentDsp}, \nfor a period of {amortizationMonths:2d} months.")

    return