from turtle import Turtle,Screen

def move_forward():
    brush.forward(10)

def move_backward():
    brush.backward(10)

def counter_clockwise():
    brush.left(10)

def clockwise():
    brush.right(10)

def clear_screen():
    brush.clear()
    brush.penup()
    brush.home()
    brush.pendown()

brush = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()

