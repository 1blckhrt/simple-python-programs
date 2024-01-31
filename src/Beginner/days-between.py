### Days Between Two Dates Calculator ###
# This is a simple calculator that calculates the amount of days between two dates
# The user is prompted to input two dates in the format YYYY-MM-DD
# The program then outputs the amount of days between the two dates

from datetime import date

def calculateTime():
    print("Please enter the first date in the order of year, month, and day, hitting enter after each entry, using numbers only.\n")

    year1 = input("Enter the first year: \n")
    month1 = input("Enter the first month: \n")
    day1 = input("Enter the first day: \n")
    
    print("\nPlease enter the second date in the order of year, month, and day, hitting enter after each entry, using numbers only.\n")

    year2 = input("Enter the second year: \n")
    month2 = input("Enter the second month: \n")
    day2 = input("Enter the second day: \n")

    try:
        year1 = int(year1)
        month1 = int(month1)
        day1 = int(day1)
        year2 = int(year2)
        month2 = int(month2)
        day2 = int(day2)
    except:
        print("ERROR: please enter dates containing only numbers! No letters, special characters, or spaces are allowed! Returning to start...\n")
        return calculateTime()
    
    try:
        date1 = date(year1, month1, day1).isoformat()
        date2 = date(year2, month2, day2).isoformat()
    except:
        print("ERROR: please enter a valid date! Returning to start...\n")
        return calculateTime()

    if date.fromisoformat(date1) > date.fromisoformat(date2):
        days_between = str(date.fromisoformat(date1) - date.fromisoformat(date2))
        print(f"\nThe amount of days between {date1} and {date2} is {days_between}.")

    elif date.fromisoformat(date1) < date.fromisoformat(date2):
        days_between = str(date.fromisoformat(date2) - date.fromisoformat(date1))
        print(f"\nThe amount of days between {date1} and {date2} is {days_between}.")

    elif date.fromisoformat(date1) == date.fromisoformat(date2):
        print(f"\nThe amount of days between {date1} and {date2} is 0 days.")

calculateTime()
