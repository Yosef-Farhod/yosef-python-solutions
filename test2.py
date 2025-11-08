import os
import time


class Manager :
    def __init__(self,first_name,last_name,email,password,status="inactive") :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def layout(self):
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Status : {self.status}")


def add_user ():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")

    return Manager(first_name,lasimport os
import time


class Manager :
    def __init__(self,first_name,last_name,email,password,status="inactive") :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def layout(self):
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Status : {self.status}")


def add_user ():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    email = input("Enter your email : ")
    password = input("Enter your password : ")

    return Manager(first_name,last_name,email,password)

print("\nWelcome to user management \n")

list_user = []

while True : 

    print("""
Choose an Action : 
1. Add new user  
2. Display all users
3. Exit 
          """)
    
    n = int(input("Enter your choice : "))

    if n == 1 :
        list_user.append(add_user())
        time.sleep(2)
        
    elif n == 2 :

        os.system("CLS")
        print("*******Date users ******")
        for i in range(len(list_user)): 
            list_user[i].layout()
        time.sleep(2)
        

    elif n == 3 : 
        print("Exit.....")
        break
    
    else : 
        print("tra agin ")
    




