
from turtle import Turtle
STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.goto(position)

    def go_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor + 20)

    def go_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor - 20)
