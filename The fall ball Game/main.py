
"""
************مرحبا بكم في لعبه الكرات المتساقطه **************
قواعد اللعبه :
تحرك المضرب يمين و يسار لالتقاط الكرات 
لو كان الشكل دائره او مربع تاخد نقطه 
لو كان مربع تاخد نقطتين 
لو كان مثلث ترجع للصفر
انما لو كان سلحفاء بيضاء لخسر اللعبه 
"""

#استوراد المكاتب
from turtle import Screen ,Turtle
from mass import Mass
from score import Score
from time import sleep
from shapes import Shape

#انشاء الشاشه 
window = Screen()
window.setup(700,700)
window.bgcolor("black")
window.title("The fall ball")
window.tracer(0)
window.listen()


mass = Mass()
score = Score()
shape = Shape()
window.onkey(mass.r_goto,"Right")
window.onkey(mass.l_goto,"Left")

shape_speed = 0.15
game_on = True
while game_on :
    sleep(shape_speed)
    window.update()
    shape.goto(shape.xcor(),shape.ycor()-10)
    shape.down()

    #لو الكره لمست المضرب
    if shape.distance(mass) < 50 and shape.ycor()<- 330 :

        #لو كانت دائره او سلحفاء ياخد 1 نقطه
        if shape.shape() == "circle"or "turtle":

            #لو كانت سلحفاء لونها ابيض اوقف اللعبه 
            if (shape.shape() == "turtle") and (shape.color()[0]=="white") :
                game_on = False
                score.game_over()
                window.bgcolor("red")

            score.add_point(1) 
        #لو كان الشكل مربع 
        if shape.shape() == "square" :
            score.add_point(2)

        if shape.shape() == "triangle":
            score.add_point(-score.total_score)
            shape_speed *= 0.8 
    else :
        shape_speed = 0.1


    #تغير شكل الكائن الحالي و انزاله من جديد
    if shape.ycor() <= -350 :
        shape.chang_shape()



window.exitonclick()