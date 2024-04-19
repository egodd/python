from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score(0)

    def score(self, points):
        self.clear()
        self.write(f"Score: {points}", False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))