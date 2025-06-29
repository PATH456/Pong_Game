from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=2, stretch_wid=10)
        self.penup()
        self.goto(pos)
        self.move_y = 40
        self.move_x = 40



    def go_up(self):
        if self.ycor() < 630:
            self.move_y = 40
            self.sety(self.ycor() + self.move_y)
        else:
            self.move_y = 0


    def go_down(self):
        if self.ycor() > -630:
            self.move_y = 40
            self.sety(self.ycor() - self.move_y)
        else:
            self.move_y = 0

    def smash(self):
        if self.xcor() < 0:
            self.setx(self.xcor() + self.move_x)
        else:
            self.setx(self.xcor() - self.move_x)





