print('''Welcome to Treasure Island\nYour mission is to find the treasure\n''')

turn_choice = input('''You're at a crossroad!!\nDo you want to turn right or left. 
                    \nType 'r' for right and 'l' for left?''').lower()

if turn_choice != "l":
    print("You fell into a hole!! Game over")
    exit()

swim_choice = input("Do you want to swim or wait. Type s for swim and w for wait? ").lower()

if swim_choice != "w":
    print("There are crocodiles!!! Game over")
    exit()

door_choice = input("Which door do you want to open?. Type r for red and y for yellow and b for blue? ").lower()

if door_choice != "y":
    print("It is a room full of fire...Game over")
    exit()

print("You win... The treasure is all yours!!!")