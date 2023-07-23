from coffee_price import CoffeePrice
from coffee_ingredients import CoffeeIngredients
from coffee_machine_data import menu, resources

class CoffeeMaker:
    
    @staticmethod
    def prepare_coffee(coffee_type,total_money) -> None:
        cost = menu[coffee_type]["cost"]
        
        if not CoffeeIngredients.check_ingredients(coffee_type):
            return
        
        if not CoffeePrice.check_cost(coffee_type, total_money, cost):
            return

        CoffeePrice.add_cost_to_money(cost)
        print(f"Here is your {coffee_type.capitalize()}. Enjoy!")
        
    
    @staticmethod
    def prepare_report() -> None:
        resource = resources
        print("The current resource levels are:")
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g\n")