# Swap two numbers
num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
print(f"Before shuffling\nNumber01= {num1}\nNumber02= {num2}")
num1,num2 = num2,num1
print(f"After shuffling\nNumber01= {num1}\nNumber02= {num2}")