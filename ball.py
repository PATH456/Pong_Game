from turtle import Turtle

class Ball:
    def __init__(self):
        self.create_ball()

    def create_ball(self):
        ball = Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.turtlesize(2, 2)
        ball.penup()
        ball.goto(0, 0)

