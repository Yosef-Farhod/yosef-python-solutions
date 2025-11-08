from ball import Ball
from score import Score
from time import sleep

window = Screen()
window.bgcolor("black")
window.setup(800,600)
window.title("Ping pong Game")
window.tracer(0)
window.listen()

r_piopl = Piopl((350,0))
l_piopl = Piopl((-350,0))
r_score = Score(50)
l_score = Score(-50)
ball = Ball()

#انشاء داله لتحديد الفائز
def exit_ball(who_win) :
    ball.x_move *= -1
    l_piopl.goto(-350,0)
    r_piopl.goto(350,0)
    ball.start()
    who_win.win()

speed = 0.05
game_on = True
while game_on :
    window.update()
    sleep(speed)

    #تحريك القطع 
    window.onkey(r_piopl.go_up,"Up")
    window.onkey(r_piopl.go_down,"Down")
    window.onkeypress(l_piopl.go_up,"w")
    window.onkeypress(l_piopl.go_down,"s")

    #تحريك الكره 
    ball.goto(ball.xcor()+ ball.x_move,ball.ycor()+ball.y_move)

    #اصتضام الكره بالاجزء 
    if (ball.xcor() >= 320 and r_piopl.distance(ball) <= 50) or (ball.xcor() <= -320 and l_piopl.distance(ball) <= 50) :
        ball.x_move *= -1
        speed *= 0.9

    #منع خروج الكره من الجزء العلوي 
    if ball.ycor() > 270 or ball.ycor() < -270 :
        ball.y_move *= -1

    #لو الكره خرجت من الجانب اليمين
    if ball.xcor() >= 430 :
        exit_ball(l_score)
        speed = 0.08

    #لو الكره خرجت من الجانب اليسار 
    if ball.xcor() <= -430 :
        exit_ball(r_score)
        speed = 0.08

    #نهايه الجيم عند 10 نقاط 
    if r_score.scores >= 3 or l_score.scores >=3 :
        game_on = False
        r_score.end()
        window.bgcolor("gold")



window.exitonclick()