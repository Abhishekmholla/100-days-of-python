import os
print("Welcome to the secret auction program")

def get_highest_bidder(bidders):
    largest_bidder_value = 0
    for key,value in bidders.items():
        if value > largest_bidder_value:
            largest_bidder = (key,value)
            largest_bidder_value = value
            
    return largest_bidder


def clear_screen():
    os.system('cls')

def add_bidders(bidders):
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid? $"))
    bidders[user_name] = user_bid
    
is_end = False
bidders = {}
while not is_end:
    
    add_bidders(bidders)
    any_other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if any_other_bidder not in ['yes','no']:
        print("Invalid input. Please provide a valid input")
        continue
    
    if any_other_bidder == 'yes':
        clear_screen()
        continue
    
    largest_bidder = get_highest_bidder(bidders)
    
    clear_screen()
    print(f"The winner is {largest_bidder[0]} with a bid of ${largest_bidder[1]}")
    is_end = True
    
        