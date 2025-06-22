# Simple Login and Profile System:
# This script simulates a basic login system using a class to store user profiles.
# It verifies the email and PIN, then displays user info if requested.

class Provile :
    def __init__(self,name,emile,langht,password) :
        self.name = name
        self.emile = emile
        self.langht = langht 
        self.password = password

Ahmed = Provile("Ahmed Ali","Ahmed12.com" ,"Arbc",9568)
jo = Provile('jo jaksom','jo549.com',"English ",1265)

print(f" *** Welcom to the app *** ")

user_emile =input("Enter your Emile : ")
user=int(input("Enter the PIN : "))

if user_emile == jo.emile and user == jo.password :
    print(f" welcom to {jo.name} ")
    see=input("Do you wont see the provile ? ( Yes or No )").lower()

    if see == "yes":
        print(f"Your name is {jo.name} \nYour emile is {jo.emile} \nYour langht is {jo.langht} ")
    else :
        print(f"ok {jo.name}") 

if user_emile == Ahmed.emile and user == Ahmed.password :
    print(f" welcom to {Ahmed.name} ")
    see=input("Do you wont see the provile ? ( Yes or No )").lower()

    if see == "yes":
        print(f"Your name is {Ahmed.name} \nYour emile is {Ahmed.emile} \nYour langht is {Ahmed.langht} ")
    else :
        print(f"ok {Ahmed.name}")   

else :
    print('pass X tyre agen ')