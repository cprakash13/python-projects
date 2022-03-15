from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.CARS = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        rand_color = random.choice(COLORS)
        new_car.color(rand_color)
        new_car.penup()
        new_car.setheading(180)
        y_cor = random.randint(-230, 230)
        new_car.goto(325, y_cor)
        self.CARS.append(new_car)

    def move(self):
        for car in self.CARS:
            car.forward(self.move_distance)
            if car.xcor() < -325:
                self.CARS.remove(car)

    def game_over(self):
        self.move_distance = 0

    def next_level(self):
        self.move_distance += MOVE_INCREMENT
