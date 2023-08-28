from turtle import Screen
import time
from player import Player
from scoreboard import ScoreBoard
from car_manager import Cars

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600,height=500)
screen.tracer(0)
screen.listen()

user = Player()
score = ScoreBoard()
cars = Cars()

screen.onkey(user.go_up,"Up")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    cars.create()
    cars.move()

    #finishing level
    if user.level_finished():
        user.reset_position()
        score.level_count()
        cars.level_up()
    
    # detect collision with car
    for car in cars.new_cars:
        if user.distance(car) < 15:
            score.game_over()
            is_game_on = False

screen.exitonclick()