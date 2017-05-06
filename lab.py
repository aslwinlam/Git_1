
def main():
    print("This program accepts a date and outputs whether or not the date is valid")
    date = input("Please enter a date in the form mm/dd/yyyy ")
    try: 
        mm, dd, yy = date.split("/")
        mm = int(mm)
        dd = int(dd)
        yy = int(yy)

        if mm < 0 and mm > 12:
            print("Please enter a valid date")
        else:
            return month(mm, dd, yy)
    except ValueError:
        print("Please enter a valid date")

def month(date, time, year):
    if date == 4 and time > 30:
        print(" Please enter a valid date")
    elif date == 6 and time > 30:
        print("Pleae enter  a valid date")
    elif date == 9 and time > 30:
        print ("Please enter a valid date")
    elif date == 11 and time > 30:
        print("Please enter a valid date")
    elif date == 2:
        return February(date, time, year)
    elif date == 1 and time > 31:
        print("Please enter a valid date")
    elif date == 3 and time > 31:
        print("Please enter a valid date")
    elif date == 5 and time > 31:
        print(" Pleae enter a valid date")
    elif date == 7 and time > 31:
        print("Please enter a valid date")
    elif date == 8 and time > 31:
        print("Please enter a valid date")
    elif date == 10 and time > 31:
        print("Please enter a valid date")
    elif date == 12 and time > 31:
        print("Please enter a valid date")
    else:
        return correct(date, time, year)

def February(date, time, year):
    # February is an exception because it only has 28 days and on leap years 29 days
    if leapYear(date, time, year) == True and time <= 29:
        return correct(date, time, year)
    elif leapYear(date, time, year) == False and time <= 28:
        return correct(date, time, year)
    else:
        print("Please enter a valid date")

def correct(date, time, year):
    print("Your date is valid,")

main()
