from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard



screen = Screen()
screen.tracer(0) #to remove the animation of squares moving one by one
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake() 
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#running game
is_game_on =True
while is_game_on:
    #as tracer doesn't show anything on screen we use update to display the objects on screen after making all changes 
    screen.update()
    time.sleep(0.1) #delays the screens and then updates it
    snake.move()

    #collision with food
    if snake.head.distance(food)<15:
        score.inc_score()
        snake.extend_snake()
        food.refresh()
    
    #collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or  snake.head.ycor() <-290:
        is_game_on = False
        score.game_over()

    #collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<15:
            is_game_on = False
            score.game_over()

screen.exitonclick()