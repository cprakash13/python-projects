from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            high_score = file.read()
            self.high_score = int(high_score)
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def calculate_high_score(self):
        if self.high_score < self.score:
            with open("data.txt", "w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.write(arg=f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
