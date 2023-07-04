print("Welcome to the love calculator")
string_check1 = "true"
string_check2 = "love"

name1=  input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

full_name  = name1 + name2

true_count = sum([full_name.count(character) for character in string_check1])
love_count = sum([full_name.count(character) for character in string_check2])

total_score = int(str(true_count) + str(love_count))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif total_score>=40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your score is {total_score}")