import pandas
import turtle 

screen = turtle.Screen()
screen.title("U.S. States")
image = "US state game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_pointer = turtle.Turtle()
state_pointer.hideturtle()
state_pointer.penup()

df = pandas.read_csv("US state game\\50_states.csv")
# df["state"] = df["state"].str.lower()
state_names = df["state"].to_list()
guessed_names = []


while len(guessed_names)<50:
    answer_state = turtle.textinput(title=f"{len(guessed_names)}/50 States Correct",prompt="What's the name of the state").title()
    missing_names = []
    if answer_state == "Exit":
        for state in state_names:
            if state not in guessed_names:
                missing_names.append(state)
        
        new_data = pandas.DataFrame(missing_names)
        new_data.to_csv("US state game/state_to_learn.csv")
        break
    if answer_state in state_names:
        guessed_names.append(answer_state)
        state_data = df[df["state"]==answer_state]
        state_pointer.goto(int(state_data.x.item()),int(state_data.y.item()))
        state_pointer.write(f"{state_data.state.item().capitalize()}")
        


