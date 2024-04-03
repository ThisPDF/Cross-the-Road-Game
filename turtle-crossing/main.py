from turtle import Screen
from turtle_game import Player
from score import ScoreBoard
import cars
from random import randint
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
turtle = Player()
score = ScoreBoard()
score.update_score()
screen.listen()
game_on = True
cars = cars.create_cars()
while game_on:
    screen.onkey(fun=turtle.move, key="space")
    if turtle.ycor() > 260:
        turtle.reset_turtle()
        score.next_level()
    for carl in cars:
        if carl.distance(turtle) < 20:
            score.game_over()
            game_on = False
    for car in cars:
        if turtle.distance(car) < 20:
            score.game_over()
            game_on = False
        boll = bool(randint(0, 1))
        if boll:
            car.move(score.level)
        if car.xcor() < -240:
            car.reset()
        screen.update()
    screen.update()
screen.exitonclick()
