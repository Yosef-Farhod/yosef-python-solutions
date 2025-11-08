from turtle import Turtle, Screen
import random

window = Screen()
window.title("Race turtle")
window.setup(900,450)
y_position =(80,0,-80)
colers = ["red","green","blue"]
turles = []

write = Turtle()
write.color("black")
write.hideturtle()

for i in range(len(colers)) :
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colers[i])
    new_turtle.goto(x=-430,y=y_position[i])
    turles.append(new_turtle)

def race():
    game_on = True
    while game_on :
        for turtle in turles:
            if turtle.xcor() >= 430 :
                game_on = False
 from turtle import Turtle, Screen
import random

window = Screen()
window.title("Race turtle")
window.setup(900,450)
y_position =(80,0,-80)
colers = ["red","green","blue"]
turles = []

write = Turtle()
write.color("black")
write.hideturtle()

for i in range(len(colers)) :
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colers[i])
    new_turtle.goto(x=-430,y=y_position[i])
    turles.append(new_turtle)

def race():
    game_on = True
    while game_on :
        for turtle in turles:
            if turtle.xcor() >= 430 :
                game_on = False
                win_turtle = turtle.pencolor()
                return win_turtle
            else :
                turtle.forward(random.randint(1,10))

user = window.textinput("Choos","Enter your choos (Red, Green, Yellwo)").lower()
race()

if user == race() :
    window.bgcolor("gold")
    write.write("You Win",align="center", font=("Arial", 25, "normal"))

else:
    window.bgcolor("magenta")
    write.write("You lost",align="center", font=("Arial", 25, "normal"))


window.exitonclick()