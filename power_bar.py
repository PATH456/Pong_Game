from turtle import Turtle

class Bar(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid= 2, stretch_len= 5)
        self.color("white")
        self.penup()
        self.goto(pos)






