'''The rules for determining whether or not a year is a leap year follow: 
Any year that is divisible by 400 is a leap year. 
Of the remaining years, any year that is divisible by 100 is not a leap year. 
Of the remaining years, any year that is divisible by 4 is a leap year. 
All other years are not leap years. 
Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year. 
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")