print("Welcome to leap year checking tool")

year = int(input("Please enter a valid year to check? "))

if year % 400 == 0 or (year % 4 ==0 and year % 100 != 0):
    print("It is a leap year")
else:
    print("It is not a leap year")