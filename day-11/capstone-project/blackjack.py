import os
from blackjack_helper_functions.calculate_result import calculate_result
from blackjack_helper_functions.print_message import print_message
from blackjack_helper_functions.add_player_cards import add_player_cards
from blackjack_helper_functions.blackjack_logo import logo

def blackjack():
    print(logo)
    player_cards = []
    computer_cards = []

    is_end = False
    for _ in range(2):
        add_player_cards(player_cards)
        add_player_cards(computer_cards)
            
    while not is_end:
        result = calculate_result(player_cards, computer_cards)
        
        print_message("Your cards are : ", player_cards)
        print_message("Computer's first card:", computer_cards[0])

        if not all(result.values()):
            print(f"{'You won' if result['player_won'] else 'Computer won'}")
            is_end = True
            break
            
        try_another_card = input("Type 'y' to get another card, type 'n' to check result: ")
        
        if try_another_card == "y":
            add_player_cards(player_cards)
            add_player_cards(computer_cards)
            continue
        else:
            result = calculate_result(player_cards, computer_cards, True)
            print(f"{'You won' if result['player_won'] else 'Computer won'}")
            is_end = True

while input("Do you want to play game of blackjack? Type 'y' for yes and 'n' for no: ").lower() == 'y':
    os.system('cls')
    blackjack()


        