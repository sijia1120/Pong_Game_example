from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle(position=(350,0))
l_paddle = Paddle(position= (-350,0))
ball = Ball()
scoreboard =ScoreBoard()

is_game_on = True
while is_game_on:
    time.sleep(0.008)
    screen.update()
    ball.move_ball()

    screen.listen()
    screen.onkey(fun=r_paddle.go_up, key="Up")
    screen.onkey(fun=r_paddle.go_down, key="Down")
    screen.onkey(fun=l_paddle.go_up, key="w")
    screen.onkey(fun=l_paddle.go_down, key="s")

    if ball.ycor() > 280 or ball.ycor()<-280:
        print("that is a wall")
        ball.bounce_ball()

    elif ball.xcor() >340 and abs(r_paddle.ycor()-ball.ycor())<40:
       print("hit the ball")
       ball.bounce_paddle()
       scoreboard.r_point()

    elif ball.xcor() <-340 and abs(l_paddle.ycor()- ball.ycor()) <40:
       print("hit the ball")
       ball.bounce_paddle()
       scoreboard.l_point()

    elif ball.xcor() >340 and abs(r_paddle.ycor()-ball.ycor()) >=40:
        print("game over")
        ball.restart_ball()

    elif ball.xcor() <-340 and abs(r_paddle.ycor()-ball.ycor()) >=40:
        print("game over")
        ball.restart_ball()



screen.exitonclick()