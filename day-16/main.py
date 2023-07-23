from coffee_price import CoffeePrice
from coffee_maker import CoffeeMaker
from menu_options import MenuOptions

coffee_options = ['espresso','latte','cappuccino']

def coffee_function_functionalities(user_option, total_money):

    if user_option == '1':
        CoffeeMaker.prepare_coffee(coffee_options[0],total_money)
    elif user_option == '2':
        CoffeeMaker.prepare_coffee(coffee_options[1],total_money)
    elif user_option == '3':
        CoffeeMaker.prepare_coffee(coffee_options[2], total_money)
    elif user_option == '4':
        CoffeeMaker.prepare_report()
        CoffeePrice.prepare_report()
    else:
        exit()
    
def main_cofee_menu():
    print("Welcome to virtual coffee maker")

    while True:
        total_money = 0

        user_choice = MenuOptions.get_user_choice()

        if not MenuOptions.valid_user_option(user_choice):
            continue
        
        if user_choice not in ['4','5']:
            total_money += MenuOptions.get_user_coins()
            
        coffee_function_functionalities(user_choice, total_money)


main_cofee_menu()