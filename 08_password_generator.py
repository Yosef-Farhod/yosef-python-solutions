# Password Generator:
# This script generates a random password based on user input.
# The user specifies how many letters, numbers, and symbols to include in the password.

#Welcom to the password Genereator
import random
import string

print('Welcom to the password Genereator !')

total_user_number=int(input('Enter the total number of characters in the password : '))
number_letter=int(input('Enter the number of letters in the password : '))
number_number=int(input('Enter the number of number in the password : '))
number_symbols=int(input('Enter the number of symbols in the password :'))

total_random=[]
if number_letter+number_number+number_symbols==total_user_number :
    total_random.append(random.choices(string.ascii_letters,k=number_letter))
    total_random.append(random.choices(string.digits,k=number_number))
    total_random.append(random.choices(string.punctuation,k=number_symbols))

    total_random=total_random[0]+total_random[1]+total_random[2]
    random.shuffle(total_random)
    finsh_pass=''.join(total_random)
    print(F"\nYour password is : {finsh_pass}\n")

else :
    print("Invalid input , the sum of letters,numbers, and symbols doesn't match the password !")

