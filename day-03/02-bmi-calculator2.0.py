height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

bmi = round(weight / (height**2))

if bmi <18.5:
    print(f"You are underweight with bmi : {bmi}")
elif bmi <25:
    print(f"You are of normal weight with bmi : {bmi}")
elif bmi < 30:
    print(f"You are overweight with bmi : {bmi}")
elif bmi <35:
    print(f"You are obese with bmi : {bmi}")
else:
    print(f"You are clinically obese with bmi : {bmi}")