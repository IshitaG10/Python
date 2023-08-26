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

def draw_spirograph(size_of_gap):
    brush.speed("fastest")
    for i in range(int(360/size_of_gap)):
        brush.color(random_color())
        brush.circle(100)
        brush.setheading(brush.heading()+size_of_gap)


draw_spirograph(5)


screen = turtle.Screen()
screen.exitonclick()