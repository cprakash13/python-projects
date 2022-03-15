from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from snake import Snake

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("My SnaKE Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
my_screen.listen()
my_screen.onkeypress(snake.up, "Up")
my_screen.onkeypress(snake.down, "Down")
my_screen.onkeypress(snake.left, "Left")
my_screen.onkeypress(snake.right, "Right")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        # is_game_on = False
        # score.game_over()
        score.calculate_high_score()
        snake.reset()

    # collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.calculate_high_score()
            snake.reset()

my_screen.exitonclick()
