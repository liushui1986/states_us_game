import turtle
import pandas as pd
import numpy as np

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv('50_states.csv')
all_states = df['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        all_states.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df['state'] == answer_state]
        t.goto(state_data['x'].item(), state_data['y'].item())
        t.write(answer_state)

data = pd.DataFrame({'state': all_states})
data.to_csv('states_to_learn.csv', index=False)
