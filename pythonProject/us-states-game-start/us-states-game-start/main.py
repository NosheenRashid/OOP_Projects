import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Map Game")
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 50:
    user_guess = screen.textinput(title=f"{len(guess_states)}/50", prompt="What's another state's name?").title()

    if user_guess == "Exit":
        # ======= List Comprehension =======
        missing_states = [state for state in all_states if state not in guess_states]
        # -------- We writing only one line instead of writing below 4 lines ------ #
        # missing_states = []
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("new_states.csv")
        break

    if user_guess in all_states:
        guess_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_guess)


screen.exitonclick()
