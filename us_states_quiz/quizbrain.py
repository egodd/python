import pandas as pd
from turtle import Turtle


class QuizBrain(Turtle):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv('50_states.csv')
        self.score = Turtle()
        self.score.penup()
        self.guessed_states = []

    def check_answer(self, guess):
        state_df = self.df.loc[self.df['state'] == guess]
        if state_df.empty:
            return False
        else:
            self.show_state(state_df)
            return True

    def show_state(self, s_pick):
        x_cor = int(s_pick.x)
        y_cor = int(s_pick.y)
        state = s_pick.state.iloc[0]
        self.guessed_states.append(state)
        self.hideturtle()
        self.penup()
        self.goto(x=x_cor, y=y_cor)
        self.hideturtle()
        self.write(state)

    def remaining_states(self):
        for s in self.guessed_states:
            self.df.loc[self.df['state'] == s, 'state'] = None
            self.df.dropna(subset=['state'], inplace=True)
            self.df.to_csv('missed_states', index=False)
