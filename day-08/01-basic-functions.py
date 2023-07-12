# Simple function
def greet():
    print("Hi")
    print("Hope you are doing well")
    
# Function with a paramater which is initilization
# Name is the parameter
# Value passed is argument
def greet_with_args(name = "default_name"):
    print(f"Hi {name}")

greet()
greet_with_args("Abhishek")
greet_with_args()