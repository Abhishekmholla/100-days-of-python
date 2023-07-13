# Simple function
def greet():
    print("Hi")
    print("Hope you are doing well")
    
# Function with a paramater which is initilization
# Name is the parameter
# Value passed is argument
def greet_with_args(name = "default_name"):
    print(f"Hi {name}")

# Functions with more than one input
def greet_with_more_than_one_parameter(name,location):
    print(f"Hello {name}, I think {location} should be cold")

greet()
greet_with_args("Abhishek")
greet_with_args()
# Written in positional argument format
greet_with_more_than_one_parameter("Abhi","melbourne")
# Written in keyword argument format
greet_with_more_than_one_parameter(name="Abhi",location="melbourne")