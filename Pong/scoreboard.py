from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
TO_WIN = 10


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.op_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'You: {self.user_score}, Computer: {self.op_score}', align=ALIGNMENT, font=FONT)


    def increase_score(self, user):
        final = Turtle()
        final.penup()
        final.goto(0, -250)
        final.color('white')
        if user == 'user':
            self.op_score += 1

        else:
            self.user_score += 1
        self.clear()
        self.update_scoreboard()
        if self.user_score >= TO_WIN:
            final.write('You Have Won', align='center', font=FONT)

            return False
        elif self.op_score >= TO_WIN:
            final.write('You Have Lost',  align=ALIGNMENT, font=FONT)
            return False
        else:
             return True

