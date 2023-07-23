from coffee_machine_data import menu
class MenuOptions:
    COST = "cost"
    COINS = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    
    @staticmethod
    def get_user_choice():
        user_option = input("Here is the list of options for you\n" +
                        f"1) Espresso     -> ${menu['espresso'][MenuOptions.COST]}\n"
                        + f"2) Latte        -> ${menu['latte'][MenuOptions.COST]}\n"
                        + f"3) Cappuccino   -> ${menu['cappuccino'][MenuOptions.COST]}\n"
                        + "4) Report\n"
                        + "5) Off\n"
                        +"Please chose any of the options: ")
        return user_option
    
    @staticmethod
    def valid_user_option(user_choice):
        if not user_choice.isdigit() or int(user_choice) not in range(6):
            print("Invalid option. Please choose a valid option to proceed")
            return False
        
        return True
    
    @staticmethod
    def get_user_coins():
        total_money = 0
        print("Please insert coins.")
        for coin_type, coin_value in MenuOptions.COINS.items():
            
            try:  
                coin_input = input(f"How many {coin_type}. Please enter a whole number? ")
            except:
                print("Please provide a valid coin value.")
                continue
            else:
                total_money += coin_value*int(coin_input)
        return total_money