from coffee_machine_dependencies.coffee_machine_data import menu, resources

MONEY = 0
INGREDIENTS = "ingredients"
COST = "cost"
RESOURCES = resources
COINS = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}


def valid_user_option(user_option):
    if not user_option.isdigit() or int(user_option) not in range(6):
        print("Invalid option. Please choose a valid option to proceed")
        return False
    
    return True


def coffee_function_functionalities(user_option, total_money):
    if user_option == '1':
        print(prepare_coffee("espresso",total_money))
    elif user_option == '2':
        print(prepare_coffee("latte",total_money))
    elif user_option == '3':
        print(prepare_coffee("cappuccino", total_money))
    elif user_option == '4':
        prepare_report()
    else:
        exit()

def prepare_report():
    print("The current resource levels are:")
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${MONEY}")

def check_ingredients(item_to_prepare):
    ingredients = dict(menu[item_to_prepare][INGREDIENTS])

    for ingredient, required_quantity in ingredients.items():
        if not check_item(ingredient, required_quantity):
            print(f"Sorry there is not enough {ingredient}")
            return False

        RESOURCES[ingredient] -= required_quantity
    
    return True


def check_cost(item_to_prepare, total_money, cost):
    if cost > total_money:
        print(
            f"Sorry {item_to_prepare} costs: ${cost} but you have provided ${total_money}. Money Refunded")
        return False
    
    print(f"Here is ${round(total_money - cost,2)} dollars in change.")
    return True


def check_item(ingredient, required_quantity):
    if required_quantity > RESOURCES[ingredient]:
        return False

    return True


def prepare_coffee(coffee_type,total_money):
    if not check_ingredients(coffee_type):
        return

    cost = menu[coffee_type][COST]
    
    if not check_cost(coffee_type, total_money, cost):
        return

    global MONEY
    MONEY += cost
    return f"Here is your {coffee_type.capitalize()}. Enjoy!"

print("Welcome to virtual coffee maker")

is_end = False
while not is_end:
    total_money = 0
    user_option = input("Here is the list of options for you\n" +
                        f"1) Espresso     -> ${menu['espresso'][COST]}\n"
                        + f"2) Latte        -> ${menu['latte'][COST]}\n"
                        + f"3) Cappuccino   -> ${menu['cappuccino'][COST]}\n"
                        + "4) Report\n"
                        + "5) Off\n"
    +"Please chose any of the options: ")
    if not valid_user_option(user_option):
        continue
    
    if user_option not in ['4','5']:
        print("Please insert coins.")
        for coin_type, coin_value in COINS.items():
            
            try:  
                coin_input = input(f"How many {coin_type}. Please enter a whole number? ")
            except:
                print("Please provide a valid coin value.")
                continue
            else:
                total_money += coin_value*int(coin_input)

    coffee_function_functionalities(user_option, total_money)
