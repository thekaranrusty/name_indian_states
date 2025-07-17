import turtle
import pandas
from states import States

screen =turtle.Screen()
screen.setup(width=830, height=950)
screen.title("India State Game")

img = "india-outline-map.gif"
screen.addshape(img)
turtle.shape(img)
state = States()

data = pandas.read_csv("india_states.csv")
states = data.state.tolist()
x = data.x.tolist()
y = data.y.tolist()

state_count = 0
answer_list = []

while state_count <32:

    answer_state = screen.textinput(title=f"{state_count}/32 Guess the State", prompt="What's another states's name:")

    for i in range(32):

        if answer_state.lower() == states[i].lower():
            state.relocate((x[i],y[i]),states[i])
            flag = 0
            for a in answer_list:
                if a == answer_state:
                    flag = 1
            if flag != 1 :
                state_count += 1
                answer_list.append(answer_state)


if state_count == 32 :
    state.win_game()


# function to get coordinates on the image for the corresponding states
# def get_mouse(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse)

#turtle.mainloop()

screen.exitonclick()

