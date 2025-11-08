from turtle import Turtle,Screen

window = Screen()
window.bgcolor('black')
window.setup(width=1000,height=1000)

sam = Turtle()
sam.shape("turtle")
sam.color("red")
sam.pensize(3)
sam.speed("fastest")

def circles () :
    sam.penup()
    sam.goto(-300,-300)
    sam.pendown()
    for _ in range(10) :
        sam.circle(40)
        sam.left(36)

def squares() :
    sam.penup()
    sam.goto(0,0)
    sam.pendown()
    for _ in range(10):
        for _ in range(4) :
            sam.forward(80)
            sam.left(90)
        sam.left(36)

def triangle(): 
    sam.penup()
    sam.goto(300,300)
    sam.pendown()
    for _ in range(10) :
        for _ in rangefrom turtle import Turtle,Screen

window = Screen()
window.bgcolor('black')
window.setup(width=1000,height=1000)

sam = Turtle()
sam.shape("turtle")
sam.color("red")
sam.pensize(3)
sam.speed("fastest")

def circles () :
    sam.penup()
    sam.goto(-300,-300)
    sam.pendown()
    for _ in range(10) :
        sam.circle(40)
        sam.left(36)

def squares() :
    sam.penup()
    sam.goto(0,0)
    sam.pendown()
    for _ in range(10):
        for _ in range(4) :
            sam.forward(80)
            sam.left(90)
        sam.left(36)

def triangle(): 
    sam.penup()
    sam.goto(300,300)
    sam.pendown()
    for _ in range(10) :
        for _ in range(3) :
            sam.forward(80)
            sam.left(120)
        sam.left(36)

circles()
squares()

triangle()



window.exitonclick()