from turtle import Turtle
FONT = ("Courier",18,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_level = 1
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-280,220)
        self.write(f"Level = {self.game_level}", align="left",font= FONT)

    def level_count(self):
        self.game_level +=  1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center",font= FONT)