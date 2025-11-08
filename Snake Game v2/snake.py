#استوراد المكتبات
from turtle import Turtle

#بدا انشاء الكلاس 
class Snake :

    #تعريفات
    def __init__(self):
        self.turtles = []
        self.posthion = [(-40,0),(-20,0),(0,0)]
        self.crite()
        self.head = self.turtles[-1]

    #انشاء جسم الثعبان 
    def crite(self) :
        for i in range(len(self.posthion)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.posthion[i])
            self.turtles.append(new_turtle)

    #انشاء داله الحركه 
    def move(self) :
        for i in range(len(self.turtles)-1) :
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)

    #انشاء داله لزياده طول الثعبان 
    def add(self) :
    #استوراد المكتبات
from turtle import Turtle

#بدا انشاء الكلاس 
class Snake :

    #تعريفات
    def __init__(self):
        self.turtles = []
        self.posthion = [(-40,0),(-20,0),(0,0)]
        self.crite()
        self.head = self.turtles[-1]

    #انشاء جسم الثعبان 
    def crite(self) :
        for i in range(len(self.posthion)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.posthion[i])
            self.turtles.append(new_turtle)

    #انشاء داله الحركه 
    def move(self) :
        for i in range(len(self.turtles)-1) :
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)

    #انشاء داله لزياده طول الثعبان 
    def add(self) :
        new_turtl = Turtle("square")
        new_turtl.color("white")
        new_turtl.penup()
        new_turtl.goto(self.turtles[0].position())
        self.turtles.insert(0,new_turtl)

    #تعريف الاتجاهات 
    def up(self) :
        self.head.setheading(90)
    def down(self) :
        self.head.setheading(270)
    def right(self) :
        self.head.setheading(0)        
    def left(self) :
        self.head.setheading(180)
    





















