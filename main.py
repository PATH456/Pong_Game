from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from power_bar import Bar
import time

game_is_on = True
power_pos1 = -880
power_pos2 = 380
full_bar1 = -280
full_bar2 = 980
energy_bar1 = []
energy_bar2 = []

my_screen = Screen()
my_screen.setup(height = 1500, width = 2500)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

#Write the borderline
border_line = Turtle()
border_line.hideturtle()
border_line.pensize(10)
border_line.penup()
border_line.color("white")
border_line.goto(0, -1000)
border_line.setheading(90)

#Draw the power bar for each paddle (930, -740), (-930, -740)
def draw_bar(pos, width = 40, length = 600):
    frame = Turtle()
    frame.pensize()
    frame.hideturtle()
    frame.penup()
    frame.color("white")
    frame.goto(pos)
    frame.setheading(90)
    frame.pendown()

    for line in range(2):
        frame.forward(width)
        frame.left(90)
        frame.forward(length)
        frame.left(90)
    return frame

bar1 = draw_bar((930, -740))
bar2 = draw_bar((-330, -740))




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
my_screen.onkey(player1.smash, "d")
my_screen.onkey(player2.smash, "Left")

while game_is_on:
    time.sleep(0.03)
    ball.move()
    if ball.ycor() > 720 or ball.ycor() < -720:
        ball.bounce_y()
    # if player2.xcor() - 25 < ball.xcor() < player2.xcor() + 25 and player2.ycor() - 120 < ball.ycor() < player2.ycor() + 120:
    if 10 < ball.distance(player2) < 90 and ball.xcor() > 1180:
        ball.bounce_x()
    # elif player1.xcor() - 25 < ball.xcor() < player1.xcor() + 25 and player1.ycor() - 120 < ball.ycor() < player1.ycor() + 120:
    elif 10 < ball.distance(player1) < 90 and ball.xcor() < -1180:
        ball.bounce_x()


    elif ball.xcor() > 1260:
        player1_score.clear_score()
        player1_score.score_update()
        player1.energy_full = False
        ball.move_x = 20
        ball.goto(0, 0)
        if power_pos1 < full_bar1:
            power_bar1 = Bar((power_pos1, -720))
            energy_bar1.append(power_bar1)
            power_pos1 += 100
    elif ball.xcor() < -1260:
        player2_score.clear_score()
        player2_score.score_update()
        player2.energy_full = False
        ball.move_x = -20
        ball.goto(0, 0)
        if power_pos2 < full_bar2:
            power_bar2 = Bar((power_pos2, -720))
            energy_bar2.append(power_bar2)
            power_pos2 += 100

    if power_pos1 == full_bar1:
        player1.energy_full = True

    if player1.xcor() > -1220:
        if player1.energy_full:
            ball.move_x = 100
        power_pos1 = -880
        for bar in energy_bar1:
            bar.hideturtle()
        player1.move_x = 1
        player1.setx(player1.xcor() - player1.move_x)
    else:
        player1.move_x = 20

    if power_pos2 == full_bar2:
        player2.energy_full = True

    if player2.xcor() < 1220:
        if player2.energy_full:
            ball.move_x = -100
        power_pos2 = 380
        for bar in energy_bar2:
            bar.hideturtle()
        player2.move_x = 1
        player2.setx(player2.xcor() + player2.move_x)
    else:
        player2.move_x = 20

    if player1_score.score > 21 or player2_score.score > 21:
        game_is_on = False
        game_over = Scoreboard((-20, -100))
        game_over.clear()
        game_over.write("Game Over", align= "center", font = ("Arial", 20, "normal"))

    my_screen.update()








my_screen.exitonclick()

