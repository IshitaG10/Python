from turtle import Turtle
with open("snake_game\data.txt") as file:
    HIGH_SCORE = file.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
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

    def game_reset(self):
        if self.score > self.high_score:
            with open("snake_game\data.txt",mode="w") as file:
                file.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align="center",font=("Courier New",20,"normal"))
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}",align="center",font=("Courier New",20,"normal"))
        

