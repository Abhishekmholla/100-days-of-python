class CoffeePrice:
    MONEY = 0
    @staticmethod
    def check_cost(item_to_prepare, total_money, cost) -> bool:
        if cost > total_money:
            print(
                f"Sorry {item_to_prepare} costs: ${cost} but you have provided ${total_money}. Money Refunded")
            return False
        
        print(f"Here is ${round(total_money - cost,2)} dollars in change.")
        return True
    
    @staticmethod
    def add_cost_to_money(cost):
        CoffeePrice.MONEY += cost
    
    @staticmethod
    def prepare_report():
        print(f"The total earnings are: ${CoffeePrice.MONEY}\n")