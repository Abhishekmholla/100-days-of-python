print("Welcome to pythonpizza deliveries!!")
bill = 0
size = input("What size of pizza do you want S for small, M for medium and L for large? ")

if size.lower() == 's':
    bill = 15
elif size.lower() == 'm':
    bill = 20
else:
    bill = 25

add_pepperoni = input("Do you want pepperoni Y for yes and N for no ?")

if add_pepperoni.lower() == 'y':
    if size.lower() != 's':
        bill += 3
    else:
        bill +=2

add_cheese = input("Do you want extra cheese Y for yes and N for no ? ") 

if add_cheese.lower() == 'y':
    bill +=1

print(f"Your final bill is : ${bill}")