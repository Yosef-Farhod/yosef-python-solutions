#استوراد المكتبات
from snake import Snake
from turtle import Screen
from time import sleep 
from food import Food
from scorbar import Scorbar

#ضبط اعدادات الشاشه 
window = Screen()
window.bgcolor("black")
window.setup(700,700)
window.tracer(0)

#انشاء المتغيرات و الكائنات
sam = Snake()
food = Food()
score = Scorbar()

game_on = Tr#استوراد المكتبات
from snake import Snake
from turtle import Screen
from time import sleep 
from food import Food
from scorbar import Scorbar

#ضبط اعدادات الشاشه 
window = Screen()
window.bgcolor("black")
window.setup(700,700)
window.tracer(0)

#انشاء المتغيرات و الكائنات
sam = Snake()
food = Food()
score = Scorbar()

game_on = True

#بدا تشغل الكود 
while game_on :
    sam.move()
    window.update()
    sleep(.1)

    #اخز الحركات من المستخدم
    window.listen()
    window.onkey(sam.up,"Up")
    window.onkey(sam.down,"Down")
    window.onkey(sam.right,"Right")
    window.onkey(sam.left,"Left")
    
    #لو الثعبان وصل للطعام
    if sam.head.distance(food) < 15 :
        sam.add()
        food.area()
        score.updat_scprlbar()

    if sam.head.xcor() >330 or sam.head.xcor() < -330 or sam.head.ycor() > 330 or sam.head.ycor()< -330 :
        game_on = False
        score.game_over()

    for i in sam.turtles[:-1] :
        if sam.head.distance(i) < 10 :
            game_on = False
            score.game_over()
    


window.exitonclick()   