from turtle import Turtle
STARTING_POSITION = [(-720, 0), (-720, -40), (-720, -80)]
class Paddle1:
    def __init__(self):
        self.segment_list = []
        self.create_paddle1()

    def create_paddle1(self):
        for pos in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.turtlesize(2,2)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segment_list.append(new_segment)

    def move_up(self):
        for seg in self.segment_list:
            seg.sety(seg.ycor() + 20)

    def move_down(self):
        for seg in self.segment_list:
            seg.sety(seg.ycor() - 20)








