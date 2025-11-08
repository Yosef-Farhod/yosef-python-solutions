from turtle import Turtle,Screen
import random

sam = Turtle()
tom = Turtle()
window = Screen()
window.setup(800,800)
window.bgcolor("black")

sam.color("red")
sam.shape("turtle")
sam.speed("fast")
sam.pensize(5)

tom.color("blue")
tom.shape("square")
tom.speed("fast")
tom.pensize(5)

my_distance = [10,20,30,40,50,60,70,80,90,100]
my_angles = [90,270]

num = random.randint(10,200)

for i in range(num) : 
    
    if num /2 > i :
        sam.forward(random.choice(my_distance))
        sam.left(random.choice(my_angles))

    else :
        tom.forward(random.choice(my_distance))
        tom.lfrom turtle import Turtle,Screen
import random

sam = Turtle()
tom = Turtle()
window = Screen()
window.setup(800,800)
window.bgcolor("black")

sam.color("red")
sam.shape("turtle")
sam.speed("fast")
sam.pensize(5)

tom.color("blue")
tom.shape("square")
tom.speed("fast")
tom.pensize(5)

my_distance = [10,20,30,40,50,60,70,80,90,100]
my_angles = [90,270]

num = random.randint(10,200)

for i in range(num) : 
    
    if num /2 > i :
        sam.forward(random.choice(my_distance))
        sam.left(random.choice(my_angles))

    else :
        tom.forward(random.choice(my_distance))
        tom.left(random.choice(my_angles))






window.exitonclick()


