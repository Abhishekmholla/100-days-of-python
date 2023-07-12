import random
import os
from hangman_dependencies.hangman_art import logo,hangman_ascii
from hangman_dependencies.hangman_words import word_list

print("Welocome to the hangman game")
print(logo)

# Constants
lives = 6
correct_word_count = 0

# Choosing a word randomly
word_selected = random.choice(word_list)
print(
    f"The word is {len(word_selected)} letter long as shown below. Trying guessing it\n")
print("_\t"*len(word_selected))

# Creating a list of _ spaces
new_word = ("_\t"*len(word_selected)).strip('\t').split('\t')


while lives != 0:
    user_input = input("\nGuess a letter: ").lower()

    os.system('cls')
    # If the user input is invalid, throw error
    if len(user_input) == 0 or len(user_input) > 1:
        print("Please enter some valid letter to proceed with the game")
        continue
    
    # If the user tries a letter already present in new word
    if user_input in new_word:
        print("You have already tried this letter. Please try a different letter")
        continue
    
    # If the user input cannot be found in the selected word, reduce one life and continue
    if user_input not in word_selected:
        print(
            f"Bad choice!! I cannot see the letter in the word. You just lost one life and only {lives-1} lives remain")
        print(hangman_ascii[abs(lives - 7)])
        lives -= 1
        if lives == 0:
            print("Hard luck...You lose")
        continue
    
    print("That's right!!! I can see the letter in the word")

    # Replacing the underscore with the value
    for index, letter in enumerate(word_selected):
        if user_input == letter:
            correct_word_count += 1
            new_word.pop(index)
            new_word.insert(index, user_input)

    if len(word_selected) == correct_word_count:
        print("You win")
        lives = 0

    print("\n"+"\t".join(new_word))


