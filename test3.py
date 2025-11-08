import os 
import time

class Gym :
    def __init__(self,first_name,last_name,id,status="inactive"):
        self.first_name = first_name 
        self.last_name =  last_name 
        self.id = id 
        self.status = status

    def show(self) : 
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Membership id : {self.id}")
        print(f"Membership Status : {self.status} \n")


def add_membership () :
    first = input("Enter first name : ")
    last = input("Enter last name : ")
    id = input("Enter membership ID : ")
    status = input("Enter membership status ,Or click enter : ")

    if not status:
       status = "inactive" 
    print("Member added successfully! ")

    return Gym(first,last,id,status)

print("\n\nWelcom to the GYM membership Mangement System ")
user_list = []

while True : 
    print("""
Choose an Action : \n      
1. Add new members 
2. Display all members
3. Search for a member 
4. Exit \n
""" )   
    
    choice = int(input("Enter your Chice : "))

    if choice == 1 : 
        user = add_membership()
        user_list.append(user)

    elif choice == 2 : 
        os.system("cls")
        print("***** Date user *****")

        for i in range(len(user_list)):
            user_list[i].show()
            print("_________________________")

    elif chimport os 
import time

class Gym :
    def __init__(self,first_name,last_name,id,status="inactive"):
        self.first_name = first_name 
        self.last_name =  last_name 
        self.id = id 
        self.status = status

    def show(self) : 
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Membership id : {self.id}")
        print(f"Membership Status : {self.status} \n")


def add_membership () :
    first = input("Enter first name : ")
    last = input("Enter last name : ")
    id = input("Enter membership ID : ")
    status = input("Enter membership status ,Or click enter : ")

    if not status:
       status = "inactive" 
    print("Member added successfully! ")

    return Gym(first,last,id,status)

print("\n\nWelcom to the GYM membership Mangement System ")
user_list = []

while True : 
    print("""
Choose an Action : \n      
1. Add new members 
2. Display all members
3. Search for a member 
4. Exit \n
""" )   
    
    choice = int(input("Enter your Chice : "))

    if choice == 1 : 
        user = add_membership()
        user_list.append(user)

    elif choice == 2 : 
        os.system("cls")
        print("***** Date user *****")

        for i in range(len(user_list)):
            user_list[i].show()
            print("_________________________")

    elif choice == 3 :
        print("Search by : \n1. Membership ID \n2. First Name \n3. Membership Status\n")
        search = int(input("Enter your choice : ")) 

        for i in range(len(user_list)):
    
            me = input("Enter the membership ID : ")
            print("***** Show date user ***")

            if  me == user_list[i].id or user_list[i].first_name or user_list[i].first_name :
                user_list[i].show()
                
            else:
                print("tyer agin")
            break
                    
    elif choice == 4 : 
        print("Exit....")
        break

    else : 
        print("Try Agin !!")
        
    time.sleep(1)