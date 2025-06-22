# Hangman Game:
# A word guessing game where the user must guess letters of a hidden word.
# The user has 6 attempts before losing. Correct guesses reveal the letters.

import random

print('\n***Welcome to the hangman game***\n')
word=['good','bad','agle']
word_random=random.choice(word)
caphir_word=["_"]*len(word_random)  

def chaa() :
    chaa=" ".join(caphir_word)
    print(chaa)
chaa()

The_number_of_attempts_left=6
#اطلب من المستخدم تاليف حرف
while "_" in caphir_word and The_number_of_attempts_left>0 :
    user_word=input('\nEnter the word : ').lower()
    for number in range(len(word_random)):
        if word_random[number]==user_word :
            caphir_word[number]=user_word
    if user_word not in caphir_word :
        The_number_of_attempts_left-=1
        
    print(f"You have {The_number_of_attempts_left}")

    chaa()

if "_" not in caphir_word :
    print('''\n          ******
          You win
          ******''')
else :
    print('''\n*You lose*
         +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''')