print("Welcome to Treasure Island\n" +
      "Your mission is to find the treasure")

turn_choice = input("Do you want to turn right or left. Type r for right and l for left? ").lower()

if turn_choice != "l":
    print("Game over")
    exit()

swim_choice = input("Do you want to swim or wait. Type s for swim and w for wait? ").lower()

if swim_choice != "w":
    print("Game over")
    exit()

door_choice = input("Which door do you want to open?. Type r for red and y for yellow and b for blue? ").lower()

if door_choice != "y":
    print("Game over")
    exit()

print("You win... The treasure is all yours!!!")