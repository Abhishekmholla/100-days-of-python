
from blackjack_helper_functions.print_message import print_message


def calculate_result(player_cards, computer_cards, is_end=False):
    result = {'player_won': True, 'computer_won': True}
    player_sum = calculate_score(player_cards)
    computer_sum = calculate_score(computer_cards)

    if player_sum > 21 or computer_sum > 21 or is_end:
        print_message("Your all cards: ", player_cards)
        print_message("Computer's all cards", computer_cards)

        if player_sum == 0 or (computer_sum > 21 and player_sum < 21):
            result['computer_won'] = False
        elif computer_sum == 0 or (player_sum > 21 and computer_sum < 21):
            result['player_won'] = False
        elif player_sum > computer_sum:
            result['computer_won'] = False
        else:
            result['player_won'] = False

    return result


def calculate_score(cards: list):
    sum_cards = sum(cards)

    if len(cards) == 2 and sum_cards == 21:
        return 0

    if 11 in cards and sum_cards > 21:
        cards.remove(11)
        cards.append(1)
        sum_cards = sum(cards)

    return sum_cards
