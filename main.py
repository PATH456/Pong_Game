from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
player1_score = Scoreboard((-612, 690))
player2_score = Scoreboard((612, 690))



my_screen.listen()
my_screen.onkey(player1.go_up, "w")
my_screen.onkey(player1.go_down, "s")
my_screen.onkey(player2.go_up, "Up")
my_screen.onkey(player2.go_down, "Down")


while game_is_on:
    time.sleep(0.03)
    ball.move()
    if ball.ycor() > 720 or ball.ycor() < -720:
        ball.bounce_y()
    if player2.distance(ball) < 50 and ball.xcor() > 1210:
        ball.bounce_x()
    #Still need to work out the logic of the bouncing ball
    if ball.xcor() > 1260:
        player1_score.clear_score()
        player1_score.score_update()
        ball.goto(0, 0)

    elif ball.xcor() < -1260:
        player2_score.clear_score()
        player2_score.score_update()
        ball.goto(0,0)

    my_screen.update()







my_screen.exitonclick()

