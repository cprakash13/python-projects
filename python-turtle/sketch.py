import random
from turtle import Turtle, Screen

new_screen = Screen()
new_screen.setup(width=500, height=400)

colors = ["blue", "green", "yellow", "orange", "red", "purple"]
racers = []
user_bet = new_screen.textinput(title="Place your bet", prompt="Which color will win the race?").lower()
is_race_on = False
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    posX = -230
    posY = -70 + i*30
    tim.goto(x=posX, y=posY)
    racers.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You won! The winning turtle is {turtle.pencolor()}")
            else:
                print(f"You lost. The winning turtle is {turtle.pencolor()}")
            break
        movement = random.randint(0, 100) % 11
        turtle.forward(movement)


new_screen.exitonclick()
