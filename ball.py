from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(x=0,y=0)
        self.speed("slowest")
        self.setheading(random.randint(-60,60))
        self.move_distance =2

    def move_ball(self):
        self.forward(self.move_distance)

    def speed_up(self):
        self.move_distance +=0.2
        print(self.move_distance)
        self.forward(self.move_distance)

    def bounce_ball(self):
        self.setheading(-self.heading())
        self.move_ball()

    def bounce_paddle(self):
        self.setheading(180-self.heading())
        self.speed_up()

    def restart_ball(self):
        self.penup()
        self.move_distance = 2
        self.setheading(self.heading()+180)
        self.goto(x=0,y=0)
        self.move_ball()