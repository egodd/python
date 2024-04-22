from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.start()
        self.x_move = 10
        self.y_move = 10

    def start(self):
        self.goto(0, 0)
        angles = [random.randint(-60, 60), random.randint(120, 240)]
        self.direction = random.choice(angles)
        # self.direction = 180
        self.setheading(self.direction)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self. y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

