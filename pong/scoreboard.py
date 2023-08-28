from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.score_display()

    def score_display(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}", align="center",font = ("Courier",40,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}", align="center",font = ("Courier",40,"normal"))

    def l_count(self):
        self.l_score += 1
        self.score_display()
    
    def r_count(self):
        self.r_score += 1
        self.score_display()