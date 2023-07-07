import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



images = [rock,paper,scissors]

user_choice = int(
    input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors..."))
computer_choice = random.randint(0, 2)

if user_choice >=3 or user_choice <0:
    print("Invalid input!! Computer wins.")
    exit()
    
print("Your Choice")
print(images[user_choice])
print("Computer choice")
print(images[user_choice])

if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
    print("You win")
elif user_choice == computer_choice:
    print("It is a draw")
else:
    print("Computer wins")
