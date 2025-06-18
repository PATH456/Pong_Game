from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(2, 2)
        self.penup()
        self.goto(0, 0)
        self.move_x = random.randint(-10, 10)
        self.move_y = random.randint(-10, 10)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
