from turtle import Turtle

class Score(Turtle) :
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.total_score = 0
        self.goto(0,300)
        self.write_s()

    def add_point(self,point) :
        self.total_score += point
        self.clear()
        self.write_s()

    def write_s(self) :
        self.write(f"score : {self.total_score}",align="center",font=("Arial",27,"normal"))  

    def game_over(self) :
        self.goto(0,0)
        self.color("black")
        self.write(f"Game over \n Your Score : {self.total_score}",align="center",font=("Arial",27,"nfrom turtle import Turtle"))

class Score(Turtle) :
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.total_score = 0
        self.goto(0,300)
        self.write_s()

    def add_point(self,point) :
        self.total_score += point
        self.clear()
        self.write_s()

    def write_s(self) :
        self.write(f"score : {self.total_score}",align="center",font=("Arial",27,"normal"))  

    def game_over(self) :
        self.goto(0,0)
        self.color("black")
        self.write(f"Game over \n Your Score : {self.total_score}",align="center",font=("Arial",27,"normal"))  

