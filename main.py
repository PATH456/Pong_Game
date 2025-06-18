from turtle import Turtle, Screen
from player1 import Paddle1
from player2 import Paddle2
from ball import Ball

my_screen = Screen()
my_screen.setup(height = 1500, width = 1500)
my_screen.bgcolor("black")
my_screen.tracer(0)

border_line = Turtle()
border_line.hideturtle()
border_line.pensize(10)
border_line.penup()
border_line.color("white")
border_line.goto(0, -1000)
border_line.setheading(90)



while int(border_line.ycor()) < 1050:
    border_line.pendown()
    border_line.forward(40)
    border_line.penup()
    border_line.forward(40)

player1 = Paddle1()
player2 = Paddle2()
ball = Ball()


def move_up():
    player1.move_up()
    my_screen.update()

def move_down():
    player1.move_down()
    my_screen.update()

def go_up():
    player2.go_up()
    my_screen.update()

def go_down():
    player2.go_down()
    my_screen.update()

my_screen.listen()
my_screen.onkey(move_up, "w")
my_screen.onkey(move_down, "s")
my_screen.onkey(go_up, "Up")
my_screen.onkey(go_down, "Down")



my_screen.update()


my_screen.exitonclick()

