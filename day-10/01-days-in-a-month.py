def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True

    return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return month_days[month - 1] + 1

    return month_days[month - 1]

def validate_month_year(month):
    if month > 12 or month < 1:
        return False
    
    return True

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

if not validate_month_year(month):
    print("Invalid month. Please provide a valid input and try again")
    exit()
    
days = days_in_month(year, month)
print(f"Number of days present = {days}")
