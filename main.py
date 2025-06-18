from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

game_is_on = True

my_screen = Screen()
my_screen.setup(height = 1500, width = 2500)
my_screen.bgcolor("black")
my_screen.title("Pong")
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

player1 = Paddle((-1220, 0))
player2 = Paddle((1220, 0))
ball = Ball()



my_screen.listen()
my_screen.onkey(player1.go_up, "w")
my_screen.onkey(player1.go_down, "s")
my_screen.onkey(player2.go_up, "Up")
my_screen.onkey(player2.go_down, "Down")


while game_is_on:
    time.sleep(0.02)
    ball.move()
    my_screen.update()
    if ball.ycor() > 720 and ball.xcor() > 0:
        ball.move_y = -10
    elif ball.ycor() > 720 and ball.xcor() < 0:
        ball.move_y = -10
        ball.move_x = -10
    elif ball.ycor() < -720 and ball.xcor() > 0:
        ball.move_x = 10
        ball.move_y = 10
    elif ball.ycor() < -720 and ball.xcor() < 0:
        ball.move_x = -10
        ball.move_y = 10
    if player1.distance(ball) < 60 or player2.distance(ball) < 60:
        if ball.xcor() < 0:
            ball.move_x = 20
        elif ball.xcor() > 0:
            ball.move_x = -20






my_screen.exitonclick()

