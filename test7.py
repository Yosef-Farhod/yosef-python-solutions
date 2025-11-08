from turtle import Turtle, Screen

window = Screen()
window.title("Python")

sam = Turtle()
sam.shape("turtle")

def cile():
    sam.color("violet")
    sam.pensize(5)
    for _ in range (3) : 
        sam.forward(100)
        sam.left(120)

def spuir() :
    sam.color("red")
    sam.pensize(10)
    for _ in range(4) :
        sam.forward(100)
        sam.left(90)
    
def circle () : 
    sam.color("black")
    sam.circle(80)

def exitt() : 
    sam.clear()
    sam.color("red")
    sam.hideturtle()
    sam.write("press any key to exit \n اضغك في اي مكان للخروج", align="center", font=("Arial", 14, "normal"))
    window.bgcolor("black")
    window.exitonclick()

chiose = " "

while True :    
    chiose = window.textinput("لحظه من فضلك ", "ما الذي تريد ان تر�from turtle import Turtle, Screen

window = Screen()
window.title("Python")

sam = Turtle()
sam.shape("turtle")

def cile():
    sam.color("violet")
    sam.pensize(5)
    for _ in range (3) : 
        sam.forward(100)
        sam.left(120)

def spuir() :
    sam.color("red")
    sam.pensize(10)
    for _ in range(4) :
        sam.forward(100)
        sam.left(90)
    
def circle () : 
    sam.color("black")
    sam.circle(80)

def exitt() : 
    sam.clear()
    sam.color("red")
    sam.hideturtle()
    sam.write("press any key to exit \n اضغك في اي مكان للخروج", align="center", font=("Arial", 14, "normal"))
    window.bgcolor("black")
    window.exitonclick()

chiose = " "

while True :    
    chiose = window.textinput("لحظه من فضلك ", "ما الذي تريد ان ترسمه ؟ (دائره, مربع , مثلث)")
    if chiose == "دائره" or (chiose == "circle"):
        circle()
    elif chiose == "مربع" or (chiose == "square") :
        spuir()
    elif (chiose == "مثلث") or chiose == "triangle" :
        cile()
    elif (chiose == "exit" ) or chiose == "خروج" :
        exitt()
    else :
            continue



window.exitonclick()
