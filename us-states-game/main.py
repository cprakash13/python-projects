import pandas as pd
from turtle import Turtle, Screen

new_screen = Screen()
image = "blank_states_img.gif"
new_screen.addshape(image)
new_screen.title("U.S. States Game")
tom = Turtle(shape=image)
pencil = Turtle()
pencil.penup()
pencil.hideturtle()
guessed_states = []
# to_be_guessed = []
data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()

while len(guessed_states) < 50:
    player_guess = new_screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What is another state's name?").title()

    if player_guess == "Exit":
        # for state in states_list:
        #     if state not in guessed_states:
        #         to_be_guessed.append(state)
        to_be_guessed = [state for state in states_list if state not in guessed_states]
        missing_states = pd.DataFrame(to_be_guessed)
        missing_states.to_csv("states_to_learn.csv")
        break

    if player_guess in states_list and player_guess not in guessed_states:
        state_data = data[player_guess == data["state"]]
        pencil.goto(int(state_data["x"]), int(state_data["y"]))
        pencil.write(arg=player_guess)
        guessed_states.append(player_guess)


# Get coordinates of mouse click
# def coordinates(x, y):
#     cor = (x, y)
#     print(cor)
# new_screen.onscreenclick(coordinates)
# turtle.mainloop()

