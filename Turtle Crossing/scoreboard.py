from turtle import Turtle

FONT = ("Courier", 24, "normal")
SUB_FONT = ("Courier", 12, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'LEVEL: {self.level}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write('Game Over', align=ALIGNMENT, font=FONT)
        self.penup()
        self.goto(0, 230)
        self.write(f'Final Score: {self.level}', align=ALIGNMENT, font=SUB_FONT)


