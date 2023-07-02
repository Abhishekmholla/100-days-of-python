# String
# This is referred to as subscripting, 
# where we are fetching an item at the specific position
print("Hello"[0])
# To fetch the last character
print("Hello"[-1])

# Integers
print(123+456)
# We can use underscore as commas and the compiler will ignore that and compile.
print(123_12324)

# To check the type of a variable
num =123
print(type(num))

# Type Casting - to change the data type of one variable from one form to another
name_length = len(input("What is your name?"))
print(f"Your name contains {str(name_length)} characters")