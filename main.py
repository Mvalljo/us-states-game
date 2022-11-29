import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses_list = []

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

while len(correct_guesses_list) != 50:
    correct_guesses_num = str(len(correct_guesses_list))
    answer_state = screen.textinput(title=correct_guesses_num + "/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        s = turtle.Turtle()
        s.penup()
        s.hideturtle()
        state_data = data[data.state == answer_state]
        s.goto(int(state_data.x), int(state_data.y))
        s.write(answer_state)
        if answer_state not in correct_guesses_list:
            correct_guesses_list.append(answer_state)

# # state_to_learn
# print(data)
# need_to_learn = []
# for num in range(50):
#     if correct_guesses_list[num] in data["state"][num]:
#         data.
#         print("hi")

# print(data)
