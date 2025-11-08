from turtle import Turtle
import random

class Shape(Turtle) :
    
    def __init__(self) :
        super().__init__()
        self.penup()
        self.squares = ["square","circle","turtle","triangle"]
        self.colors = ["red","green","gold","blue","yellow","orange","pink","brown"]
        self.sizes = [0.5,1,1,1,2]
        self.chang_shape()
            
    def down(self) :
        self.goto(self.xcor(),self.ycor()-10)

    def chang_shape(self):
        self.hideturtle()
        self.goto(random.randint(-300,300),360)
        self.shape(random.choice(self.squares))
        self.color(random.choice(self.colors))
        self.shapesize(random.choice(self.sizefrom turtle import Turtle
import random

class Shape(Turtle) :
    
    def __init__(self) :
        super().__init__()
        self.penup()
        self.squares = ["square","circle","turtle","triangle"]
        self.colors = ["red","green","gold","blue","yellow","orange","pink","brown"]
        self.sizes = [0.5,1,1,1,2]
        self.chang_shape()
            
    def down(self) :
        self.goto(self.xcor(),self.ycor()-10)

    def chang_shape(self):
        self.hideturtle()
        self.goto(random.randint(-300,300),360)
        self.shape(random.choice(self.squares))
        self.color(random.choice(self.colors))
        self.shapesize(random.choice(self.sizes))
        self.showturtle()
        self.down()

 
                    
