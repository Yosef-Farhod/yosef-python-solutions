from turtle import Turtle

class Score(Turtle) :
    def __init__(self,pothtion) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scores = 0
        self.goto(pothtion,250)
        self.score()

    def score(self) :
        self.write(f"{self.scores}",align="center",font=("Arial",28,"normal"))

    def win(self) :
      from turtle import Turtle

class Score(Turtle) :
    def __init__(self,pothtion) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scores = 0
        self.goto(pothtion,250)
        self.score()

    def score(self) :
        self.write(f"{self.scores}",align="center",font=("Arial",28,"normal"))

    def win(self) :
        self.clear()
        self.scores += 1
        self.score()

    def end(self):
        self.color("black")
        self.goto(0,0)
        self.write(f"The End \ncongratulation",align="center",font=("Arial",28,"normal"))

