shapeclass Recise : 
    def __init__(self,name,ingredients,time,instructions):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def information(self) : 
        print()
        print(f"Name : {self.name}")
        print(f"Ingredients : {self.ingredients}")
        print(f"Cosking time : {self.time}")
        print(f"Instructions : {self.instructions}")


def input_user() : 
    print("\nDisplaying recipe ......")
    name = input("Enter recipe name : ")
    ingredients = input("Enter ingredients : ")
    time = input("Enter cooking time : ")
    instructions = input("Enter cooking instructions : ")
    print("Recipe added successfuly!  ")
    return Recise(name,ingredients,time,instructions)


re1 = input_user()
re1.information()

