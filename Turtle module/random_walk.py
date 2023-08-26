import turtle
import random 


brush = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color

directions = [0,90,180,270]
brush.width(15)
brush.speed("fastest")

for i in range(200):
    brush.color(random_color())
    brush.forward(30)
    brush.setheading(random.choice(directions))



screen = turtle.Screen()
screen.exitonclick()