from turtle import Turtle
class Mass(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.penup()
        self.goto(0,-310)
        self.l_goto()
    
    def r_goto(self) :
        new_x = self.xcor()
        if new_x < 330 :
            new_x += 40
            self.goto(new_x,self.ycor())
        else:
            self.goto(new_x-20,self.ycor())
    
    def l_goto(self) :
        new_x = self.xcor()
        if new_x > -320 :
            new_x += -40
            self.goto(new_x,self.ycor())
        else:
            self.goto(new_x-20,self.ycor())
class Mass(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.penup()
        self.goto(0,-310)
        self.l_goto()
    
    def r_goto(self) :
        new_x = self.xcor()
        if new_x < 330 :
            new_x += 40
            self.goto(new_x,self.ycor())
        else:
            self.goto(new_x-20,self.ycor())
    
    def l_goto(self) :
        new_x = self.xcor()
        if new_x > -320 :
            new_x += -40
            self.goto(new_x,self.ycor())
        else:
            self.goto(new_x-20,self.ycor())
