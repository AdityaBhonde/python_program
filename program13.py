def is_leap_year(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print(str(year)+"the year is a leap year ")
    else:
        print(str(year)+"the year is  not a leap year ")

ivalue = int(input("enter the year "))

is_leap_year(ivalue)


     
