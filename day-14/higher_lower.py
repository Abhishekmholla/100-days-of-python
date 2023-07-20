import os
import random
from higher_lower_art import logo, vs
from higher_lower_data import data

score = 0
is_end = False


def validate_user_choice(user_choice):
    if user_choice not in ['a', 'b']:
        return False

    return True


def calculate_result(user_choice, compare_item_one, compare_item_two,):

    if (user_choice == 'a' and (compare_item_one['follower_count'] >= compare_item_two['follower_count'])) or (user_choice == 'b' and (compare_item_one['follower_count'] <= compare_item_two['follower_count'])):
        return True

    print(f"Your score is: {score}")
    print("You lose!! Thanks for playing")
    return False

def check_if_same_item_selected(compare_item_one, compare_item_two):
    if compare_item_one == compare_item_two:
        return True
    
    return False

print(logo)

compare_item_one = random.choice(data)
compare_item_two = random.choice(data)

if check_if_same_item_selected(compare_item_one, compare_item_two):
    compare_item_two = random.choice(data)

while not is_end:
    compare_item_two = random.choice(data)
    
    if check_if_same_item_selected(compare_item_one, compare_item_two):
        compare_item_two = random.choice(data)

    print(
        f"\nCompare A: {compare_item_one['name']},a {compare_item_one['description']}, from {compare_item_one['country']}\n")

    print(vs)

    print(
        f"Against B: {compare_item_two['name']},a {compare_item_two['description']}, from {compare_item_two['country']}\n")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if not validate_user_choice(user_choice):
        print("Invalid input. Please provide a valid input!!")
        continue

    if calculate_result(user_choice, compare_item_one, compare_item_two):
        os.system('cls')
        score +=1
        print(f"Your score is {score}")
        compare_item_one = compare_item_two
        continue

    is_end = True
