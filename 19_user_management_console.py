# User Management Console App:
# This script defines a basic user management system using a class structure.
# Users can be added with personal details, and their data can be displayed.
# The program continues until the user chooses to exit.

class Mamagement :
    def __init__(self,choice,first_name,last_name,email,password,status='incolod') : 
        self.choice =choice 
        self.first_name =first_name 
        self.last_name = last_name 
        self.email =email 
        self.password = password 
        self.status = status

def user_input() :
    choice = input('\nEnter your choice : ')
    first_name = input('Enter first name :')
    last_name = input('Enter last name : ') 
    email = input ('Enter email : ')
    password = input('Enter password : ')

    return Mamagement(choice,first_name,last_name,email,password)

def shoo (date) :
    print(f"Choice : {date.choice}")
    print(f"first name  {date.first_name}")
    print(f"Last name : {date.last_name}")
    print(f"Email : {date.email}")
    print(f"Status :{date.status} ")

    print("_____________________________________")
import os
#choose_input =int(input('\nChoose an Action : \n1. Add new User \n2. Desplay all user \n3. Exit \n\nEnter your choose : '))
choose_input = 0
date_user =[]
while choose_input != 3 :
    choose_input =int(input('\nChoose an Action : \n1. Add new User \n2. Desplay all user \n3. Exit \n\nEnter your choose : '))

    if choose_input == 1 :  
        user1 = user_input()
        date_user.append(user1)

    elif choose_input == 2 :
        os.system('cls')
        print(''' Date User
______________''')
        
        for namber in range(0,len(date_user)) :
            shoo(date_user[namber])
    else :
        print('Good bay !')
        exit
