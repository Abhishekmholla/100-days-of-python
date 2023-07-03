print("Welcome to the tip calculator")
bill_amount = float(input("What is the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

total_bill = bill_amount + bill_amount * (tip_percentage /100)

bill_per_person = round((total_bill / number_of_people),2)

print(f"Each person should pay: $ {bill_per_person}")