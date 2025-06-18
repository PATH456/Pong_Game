from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=2, stretch_wid=10)
        self.penup()
        self.goto(pos)



    def go_up(self):
        self.sety(self.ycor() + 40)

    def go_down(self):
        self.sety(self.ycor() - 40)








