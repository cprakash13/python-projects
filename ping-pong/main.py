from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

new_screen = Screen()
new_screen.bgcolor("black")
new_screen.setup(width=800, height=600)
new_screen.title("Ping-Pong")
new_screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
score = ScoreBoard()
new_screen.listen()

new_screen.onkeypress(left_paddle.go_up, "w")
new_screen.onkeypress(left_paddle.go_down, "s")
new_screen.onkeypress(right_paddle.go_up, "Up")
new_screen.onkeypress(right_paddle.go_down, "Down")

is_game_on = True
while is_game_on:
    new_screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -265:
        ball.bounce_y()
    if 340 < ball.xcor() and ball.distance(right_paddle) < 60 \
            or ball.xcor() < -340 and ball.distance(left_paddle) < 60:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -350:
        ball.refresh()
        score.r_point()













new_screen.exitonclick()