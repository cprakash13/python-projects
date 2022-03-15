import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
cars = CarManager()

screen.onkeypress(player.move_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    cars.move()
    screen.update()
    counter += 1
    if not counter % 6:
        cars.create_car()
    for car in cars.CARS:
        if car.distance(player) < 25:
            cars.game_over()
            score.game_over()
            game_is_on = False
        if player.ycor() > 260:
            player.refresh()
            score.update()
            cars.next_level()



screen.exitonclick()
