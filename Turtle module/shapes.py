import turtle
import random 

brush = turtle.Turtle()
colors = ["DarkOrchid","DeepPink","aquamarine"]

def draw_shape(num_sides):
    angle = 360/num_sides
    brush.color(random.choice(colors))
    for _ in range(num_sides):
        brush.forward(100)
        brush.right(angle)


for sides in range(3,11):
    draw_shape(sides)



screen = turtle.Screen()
screen.exitonclick()