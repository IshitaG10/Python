import colorgram
import turtle
import random

brush = turtle.Turtle()
turtle.colormode(255)
brush.hideturtle()
brush.penup()

colors = colorgram.extract('Hirst Painting/image.jpg', 20)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


y_axis = -200
brush.setx(-250)
brush.sety(y_axis)
brush.speed("fastest")
for i in range(1,100+1):
    brush.color(random.choice(rgb_colors))
    brush.dot(15)
    brush.forward(50)
    y_axis += 5
    if(i%10==0):
        brush.setx(-250)
        brush.sety(y_axis)


screen = turtle.Screen()
screen.exitonclick()
