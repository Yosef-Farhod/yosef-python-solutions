# Guess the Number Game:
# The user tries to guess a random number between 1 and 10.
# After each guess, the program gives a hint until the correct number is guessed.

import random
password = random.randint(1,10)
num = 1

print('\n*** Welcom to Guess the Number Game ***\n')

user=int(input('Guess a number btween( 1 : 10 )  : '))
while user!= password :

    if user> password :
        user=int(input('To high ! Guess agan :'))
    else :
        user=int(input('To low ! Guess agan :'))

    num +=1

print(f"🎉 Congratulations! You guessed the number in {num}")