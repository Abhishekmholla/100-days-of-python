import random


print("Welocome to the hangman game")
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Constants
lives = 6
correct_word_count = 0
random_words = '''Hello bobby This is Abhishek'''

word_selected = random.choice(random_words.lower().split())
print(
    f"The word is {len(word_selected)} letter long as shown below. Trying guessing it\n")
print("_\t"*len(word_selected))

new_word = ("_\t"*len(word_selected)).strip('\t').split('\t')


while lives != 0:
    user_input = input("\nGuess a letter: ")

    if len(user_input) == 0 or len(user_input) > 1:
        print("Please enter some valid letter to proceed with the game")
        continue

    if user_input not in word_selected:
        print(
            f"Bad choice!! I cannot see the letter in the word. You just lost one life and only {lives-1} lives remain")
        print(hangman_ascii[abs(lives - 7)])
        lives -= 1
        continue

    print("That's right!!! I can see the letter in the word")

    for index, letter in enumerate(word_selected):
        if user_input == letter:
            correct_word_count += 1
            new_word.pop(index)
            new_word.insert(index, user_input)

    if len(word_selected) == correct_word_count:
        lives = 0

    print("\n"+"\t".join(new_word))
