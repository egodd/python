from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import random
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor('blue')
my_screen.title("Play Pong")
my_screen.tracer(0)

# create objects
my_paddle = Paddle()
op_paddle = Paddle()
scores = ScoreBoard()

# divider
divider = Turtle('square')
divider.color('white')
divider.shapesize(20, .1)


def paddle_reset():
    op_paddle.start_location(360)
    my_paddle.start_location(-360)

paddle_reset()

my_screen.listen()
my_screen.onkey(my_paddle.up, "Up")
my_screen.onkey(my_paddle.down, "Down")

is_ball = False
game_is_on = True

while game_is_on:
    my_screen.update()
    if not is_ball:
        my_screen.update()
        my_ball = Ball()
        is_ball = True

    time.sleep(0.08)
    my_ball.move()

    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_wall()

    if my_ball.ycor() > op_paddle.ycor() and my_ball.xcor() > 0:
        move = random.randint(1, 3)
        if move == 2:
            op_paddle.up()
    elif my_ball.ycor() < op_paddle.ycor() and my_ball.xcor() > 0:
        move = random.randint(1, 3)
        if move == 2:
            op_paddle.down()

    if my_ball.distance(op_paddle) < 50 and my_ball.xcor() > 340 or my_ball.distance(my_paddle) < 50 and my_ball.xcor() < -340:
        my_ball.bounce_paddle()

    if my_ball.xcor() <= my_paddle.xcor() - 20:
        game_is_on = scores.increase_score('user')
        my_ball.start()
        paddle_reset()


    if my_ball.xcor() >= op_paddle.xcor() + 20:
        game_is_on = scores.increase_score('op')
        my_ball.start()
        paddle_reset()





my_screen.exitonclick()
