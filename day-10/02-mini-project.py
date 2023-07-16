import os

print("Welcome to My Calculator")

def validate_number(number):
    try:
        if float(number):
            return True
    except ValueError:
        return False

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number
    total = 0
    if operation == '+':
        total = add(first_number, second_number)
        print(
            f"{first_number} {operation} {second_number} = {total}")
    elif operation == '-':
        total = subtract(first_number, second_number)
        print(
            f"{first_number} {operation} {second_number} = {total}")
    elif operation == '*':
        total = multiply(first_number, second_number)
        print(
            f"{first_number} {operation} {second_number} = {total}")
    elif operation == '/':
        total = divide(first_number, second_number)
        print(
            f"{first_number} {operation} {second_number} = {total}")
    return total

first_number = 0
operations = {
    '+': add,
    '-':subtract,
    '*': multiply,
    '/':divide
}

while True:

    if int(first_number) == 0:
        first_number = float(input("What's the first number?: "))

    print("You have the following operations at your disposal +,-,*,/")
    operation = input("Pick an opertion from the above list: ")

    second_number = float(input("What's the second number?: "))

    if not (validate_number(first_number) or validate_number(second_number)):
        print("Please enter a valid number to continue.")
        continue

    if operation not in ['+', '-', '*', '/']:
        print("Please provide a valid operation to continue.")
        continue
    
    calculation_function = operations[operation]
    
    total = calculation_function(first_number,second_number)
    
    print(f"{first_number} {operation} {second_number} = {total}")
    is_continue = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation or 'e' to exit: ").lower()
    
    if is_continue == 'y':
        first_number = total
        continue
    elif is_continue == 'n':
        os.system('cls')
        first_number = 0
        continue
    elif is_continue == 'e':
        exit()
    else:
        first_number = 0
        print("Invalid operation")
        continue