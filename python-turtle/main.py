import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    chosen_color = (r, g, b)
    return chosen_color


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy = Turtle()
timmy.pensize(3)
timmy.speed("fastest")
turtle.colormode(255)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(25)
for _ in range(50):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(360/50)



new_screen = Screen()
new_screen.exitonclick()
