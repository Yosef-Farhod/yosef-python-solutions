# Hangman Game (with ASCII Graphics):
# A word guessing game where the user guesses letters of a word.
# Each wrong guess reduces a life and displays a part of the hangman.
# The user wins by guessing all letters before running out of lives.

import random

HANGMANPICS = ['''
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
print('*** welcome to the Game Hangeman ')
word=['good','bad','agle']
word_random=random.choice(word)

chiss=['_']*len(word_random)
print(" ".join(chiss))
print(HANGMANPICS[0])

lives=6
phiot=0
wrong_words=[]

while "_" in chiss and lives > 0 :

    user_input=input('\nEnter the word :  ')
    for number in range(len(word_random)) :
        if word_random[number] ==user_input :
            chiss [number] = user_input
    print(" ".join(chiss))

    if user_input not in word_random :
      if user_input not in wrong_words :
        lives-=1
        phiot+=1
        wrong_words.append(user_input)
      else :
        print(f"you choce the ( {user_input} ) befor that .")
        continue
      
      print(f"Tyr agan you have {lives}")
      print(HANGMANPICS[phiot])
    
    else :
      print(f"Good you have {lives}")
    print("___________________________________")
      

if lives > 0 :
  print ('''
  ***********
    You Win 
  ***********
  ''')
else :
  print('''
  ************
    You Lost
  ************  
  ''')
  print(HANGMANPICS[phiot])
    













