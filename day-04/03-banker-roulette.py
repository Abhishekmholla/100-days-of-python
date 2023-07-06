import random

names = input("Please enter all the names in comma seperated form. ").split(', ')
print(f"{random.choice(names)} has to pay the bill")