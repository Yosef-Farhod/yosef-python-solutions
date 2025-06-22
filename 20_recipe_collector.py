# Recipe Collector:
# This script allows the user to enter a cooking recipe,
# including its name, ingredients, cooking time, and instructions.
# It then displays the recipe details back to the user.

class Recipe :
    def __init__(self,name,intredients,time,instructions) : 
        self.name = name 
        self.intredients = intredients 
        self.time = time 
        self.instructions = instructions 
        
def user_input () :
    print(' Welcom to Recipe Collection ')
    name = input('Enter recie name : ')
    intredients = input ('Enter Intredients : ')
    time = input('Enter Cooking Time : ')
    instructions = input ('Enter Cooking instructions : ')

    return Recipe(name,intredients,time,instructions)


def cooking_print(numes) :
    print('\nRecuoe add successfully ')
    print(f"Name : {numes.name} ")
    print(f"Intredients : {numes.intredients} ")
    print(f"Cooking time : {numes.time} ")
    print(f"Instructions : {numes.instructions}")

first_recie = user_input()
cooking_print(first_recie)