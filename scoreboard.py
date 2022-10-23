from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreSx = 0
        self.scoreDx = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.scoreSx} | {self.scoreDx}", align=ALIGNMENT, font=FONT)

    def increase_score(self, isLeftPlayer):
        if isLeftPlayer:
            self.scoreSx += 1
        else:
            self.scoreDx += 1
        self.update_scoreboard()
