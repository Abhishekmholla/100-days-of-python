height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

bmi = round(weight / (height**2),2)

print(f"Your bmi is {bmi}")