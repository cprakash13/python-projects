from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 260)
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))
