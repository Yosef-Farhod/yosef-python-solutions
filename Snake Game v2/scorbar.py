from turtle import Turtle 
 
 #creat class
class Scorbar(Turtle) :
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.high_score =  0
        self.write_scorbar() 
    
    def write_scorbar(self) :
        self.write(f"Score : {self.score}    High Score{self.high_score}",align="center",font=("Arial",24,"normal"))

    def updat_scprlbar(self) :
        self.score += 1
        self.clear()
        self.write_scorbar()

    def game_over(self) :
        self.goto(0,0)
        self.clear()
        self.screen.bgcolor("red")
        if self.sfrom turtle import Turtle 
 
 #creat class
class Scorbar(Turtle) :
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.high_score =  0
        self.write_scorbar() 
    
    def write_scorbar(self) :
        self.write(f"Score : {self.score}    High Score{self.high_score}",align="center",font=("Arial",24,"normal"))

    def updat_scprlbar(self) :
        self.score += 1
        self.clear()
        self.write_scorbar()

    def game_over(self) :
        self.goto(0,0)
        self.clear()
        self.screen.bgcolor("red")
        if self.score > self.high_score :
            self.high_score = self.score
        self.write(f"---------Game Over ---------\n\nScore : {self.score} \n\n High Score = {self.high_score}",align="center",font=("Arial",24,"normal"))
