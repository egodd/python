import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()

car_list = []
car_object = []

for car in car_list:
    car = CarManager()
    car_object.append(car)

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
i = 0
car_create = 0

car_speed_increase = False
increase_amount = 0
create_frequency = 10

while game_is_on:
    car_create = random.randint(1, round(create_frequency))
    if car_create == 1:
        i += 1
        car_list.append('car{}'.format(i))
        if len(car_list) > len(car_object):
            count = 0
            for car in car_list:
                count += 1
                if count == len(car_list):
                    car = CarManager()
                    car_object.append(car)
                    if car_speed_increase:
                        if create_frequency > 4:
                            create_frequency -= 0.1
                        increase_amount += 1
                        car_speed_increase = False

    for car in car_object:
        car.move(increase_amount)
        if car.xcor() <= -400:
            del car
            del car_list[0]
            del car_object[0]

    for car in car_object:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

    if turtle.ycor() >= 260:
        score.increase_score()
        turtle.restart()
        for c in car_object:
            c.hideturtle()
            c.goto(-200, car.ycor())
        car_speed_increase = True


    time.sleep(0.1)
    screen.update()

screen.exitonclick()
