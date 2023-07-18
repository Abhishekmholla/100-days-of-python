import random

EASY_DIFFICULTY = 5
HARD_DIFFICULTY = 10

def validate_user_guess(number):
    if not number.isdigit():
        return False
    return True

def check_result(chosen_number,number):
    if chosen_number > number:
        print("Too low")
        return False
    elif chosen_number < number:
        print("Too high")
        return False
    else:
        print(f"You got it!! The answer is {chosen_number}")
        return True
    
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100")

chosen_number = random.randint(1,100)

difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

no_of_chances =  EASY_DIFFICULTY if difficulty_type == 'easy' else HARD_DIFFICULTY

print(f"You have {no_of_chances} attempts to guess the number")

while no_of_chances != 0:
    
    user_guess = input("Make a guess: ")
    
    if not validate_user_guess(user_guess):
        print("Invalid input. Please provide a number to continue")
        continue
    
    if not check_result(chosen_number, int(user_guess)):
        print("Guess again")
        no_of_chances -=1
        if no_of_chances == 0:
            print("You have run out of guesses, you lose")
            break
        print(f"You have {no_of_chances} attempts remaining to guess the number.")
        continue
    
    no_of_chances = 0