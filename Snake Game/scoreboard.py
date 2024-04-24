from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.points_scored = 0
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score: {self.points_scored} High Score: {self.high_score}", False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.points_scored += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.points_scored > self.high_score:
            self.high_score = self.points_scored
            with open("highscore.txt", mode="w") as self.high_score_file:
                self.high_score_file.write(str(self.high_score))

        self.points_scored = 0
        self.score()
