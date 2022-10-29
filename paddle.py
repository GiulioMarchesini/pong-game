from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, screen_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed('fastest')
        self.screen_height = screen_height

    def move_up(self):
        if self.ycor() < (self.screen_height/2 - 50):
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -(self.screen_height/2 - 50):
            self.sety(self.ycor() - 20)