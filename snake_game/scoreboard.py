from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,274)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier New",20,"normal"))
        
    def update_scoreboard(self):
        self.write(f"Score = {self.score}",align="center",font=("Courier New",20,"normal"))
        

