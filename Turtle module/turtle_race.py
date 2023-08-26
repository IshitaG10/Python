from turtle import Turtle,Screen
import random

game_on = True
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make a bet",prompt="Which color do you think will win the race?")
color = ["purple","blue","green","yellow","orange","red"]
y_axis = [-70,-40,-10,20,50,80]
turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(x = -230,y = y_axis[i])
    turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            game_on = False
            winning_color = turtle.pencolor()
            if user_bet==winning_color:
                print(f"You've won. The winner is {winning_color}")
            else:
                print(f"You've lost. The winner is {winning_color}")
                
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        
    

screen.exitonclick()