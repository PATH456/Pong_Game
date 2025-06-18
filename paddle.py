from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.turtlesize(2, 2)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)



    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)








