from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.goto(300, random.randint(-220, 220))
        self.in_game = True

    def move(self, increase):
        self.forward(MOVE_INCREMENT + increase)

    def __del__(self):
        pass


