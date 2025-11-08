from turtle import Turtle,Screen
from time import sleep 
import random

window= Screen()
window.bgcolor("black")
window.tracer(0)
position = [(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
tui = (0,1,2,3,4,5,6)
angles = (90,0,0,0,0)
turtles = []

for i in range(len(position)) :
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position[i])
    turtles.append(new_turtle)

game_on = True
whilefrom turtle import Turtle,Screen
from time import sleep 
import random

window= Screen()
window.bgcolor("black")
window.tracer(0)
position = [(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
tui = (0,1,2,3,4,5,6)
angles = (90,0,0,0,0)
turtles = []

for i in range(len(position)) :
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position[i])
    turtles.append(new_turtle)

game_on = True
while game_on :
    for i in range(len(turtles)-1) :
        turtles[i].goto(turtles[i+1].pos())
        window.update()
    turtles[-1].forward(10)
    turtles[-1].left(random.choice(angles))
    window.update()
    sleep(0.1)

   






window.exitonclick()