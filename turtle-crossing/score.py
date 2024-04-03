from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-50, 260)
        self.level = 1

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=("Courier", 20, "bold"))

    def next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(-100, 0)
        self.write(arg=f"Game Over", font=("Courier", 40, "bold"))
