from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard



screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(height=600,width=800)
screen.listen()
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()



screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on  = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with the paddles 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect r paddle miss
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_count()


    #detect l paddle miss
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_count()
    

screen.exitonclick()