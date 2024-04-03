from turtle import Turtle
from random import randrange, random


class Car(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        r = random()
        g = random()
        b = random()
        self.color(r, g, b)
        self.penup()
        self.goto(300, y_position)
        self.setheading(180)

    def move(self, level):
        dist = randrange(9, 21)
        self.forward(dist * (level + 1))

    def reset(self):
        self.goto(300, randrange(-240, 280))


def create_cars():
    cars = []
    dist = randrange(20, 50)
    for i in range(-240, 280, dist):
        car = Car(i)
        cars.append(car)
    return cars
