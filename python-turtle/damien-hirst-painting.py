# import colorgram
#
# colors = colorgram.extract("spot-painting.jpg", 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_value = (r, g, b)
#     colors_list.append(rgb_value)
# print(colors_list)
import random
import turtle
from turtle import Turtle, Screen

colors_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
timmy = Turtle()
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
timmy.goto(-250, -250)
timmy.speed(0)
for row in range(10):
    for col in range(10):
        random_color = random.choice(colors_list)
        timmy.dot(20, random_color)
        timmy.forward(50)
    y = timmy.ycor()
    y += 50
    timmy.goto(-250, y)
new_screen = Screen()
new_screen.exitonclick()
