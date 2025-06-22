# Animal Inheritance Demo:
# This script demonstrates object-oriented programming using inheritance.
# It defines a base class Animal, and subclasses for Mammals, Birds, and Fish,
# each with their own specific attributes and behaviors.

class Animal :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"The {self.name} eat....")

    def sleep (self):
        print(f"The {self.name} sleep...")

class Mammal(Animal) :
    def __init__(self, name, age,diet,weight):
        super().__init__(name, age)
        self.diet = diet
        self.weight = weight

    def walk(self):
        print(f"The {self.name} walk...")
    

class Bird(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def fly(self):
        print(f"The {self.name} fly....")
    def tweet(self):
        print(f"The {self.name} tweet.....")

class Fish(Animal):
    def __init__(self, name, age,length,nb_fin):
        super().__init__(name, age)
        self.length =length
        self.nb_fin =nb_fin

    def swim(self):
        print(f"The {self.name} swim....")
    
lion=Mammal("lion",10,"meet",150)
hood = Bird('hood',2,'yellow')
tona=Fish('tona',1,160,3)
