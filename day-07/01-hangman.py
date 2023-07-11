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

lives = 6
random_words = '''Hello bobby This is Abhishek'''

word_selected = random.choice(random_words.lower().split())
print(f"The word is {len(word_selected)} letter long as shown below. Trying guessing it\n")
print("_\t"*len(word_selected))
          
while lives != 0:

    user_input = input("\nGuess a letter: ")
    
    if len(user_input) == 0 or len(user_input) > 1:
        print("Please enter some valid letter to proceed with the game")
        break
    
    new_word = []
    if user_input in word_selected:
        print("That's right!!! I can see the letter in the word")
        for letter in word_selected:
            if user_input != letter and letter not in new_word:
                new_word.append('_')
                continue
            new_word.append(letter)

        print("\n"+"\t".join(new_word))
    else:
        print("Bad choice!! I cannot see the letter in the word")
        print(hangman_ascii[abs(lives - 6)])
        lives-= 1
        