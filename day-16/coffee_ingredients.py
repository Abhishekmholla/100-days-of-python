from coffee_machine_data import menu, resources

class CoffeeIngredients:
    RESOURCES = resources
    INGREDIENTS = "ingredients"
    COST = "cost"
    
    @staticmethod
    def check_ingredients(item_to_prepare) -> bool:
        ingredients = dict(menu[item_to_prepare][CoffeeIngredients.INGREDIENTS])

        for ingredient, required_quantity in ingredients.items():
            if not CoffeeIngredients.check_item(ingredient, required_quantity):
                print(f"Sorry there is not enough {ingredient}")
                return False

            CoffeeIngredients.RESOURCES[ingredient] -= required_quantity
        
        return True
    
    def check_item(ingredient, required_quantity) -> bool:
        if required_quantity > CoffeeIngredients.RESOURCES[ingredient]:
            return False

        return True