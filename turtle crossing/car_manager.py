from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars():
    def __init__(self):
        self.new_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create()
        

    def create(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=1.5,stretch_wid=0.7)
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-200,200)
            new_car.goto(280,y_pos)
            self.new_cars.append(new_car)
        

    def move(self):
        for car in self.new_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10
