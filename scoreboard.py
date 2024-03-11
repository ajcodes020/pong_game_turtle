from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, ALIGNMENT, FONT)

    def increase_rscore(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_lscore(self):
        self.l_score += 1
        self.update_scoreboard()