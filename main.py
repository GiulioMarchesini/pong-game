from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create a screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#creae a paddle
paddleSx = Paddle(position=(-(SCREEN_WIDTH/2 -50), 0), screen_height=SCREEN_HEIGHT)
paddleDx = Paddle(position=((SCREEN_WIDTH/2 -50), 0), screen_height=SCREEN_HEIGHT)

#listen to the keyboard
screen.listen()
screen.onkeypress(paddleSx.move_up, "w")
screen.onkeypress(paddleSx.move_down, "s")
screen.onkeypress(paddleDx.move_up, "Up")
screen.onkeypress(paddleDx.move_down, "Down")

ball=Ball()#create a ball

scoreboard = Scoreboard()#create a scoreboard

#main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    #detect collision with wall
    if ball.ycor() > (SCREEN_HEIGHT/2 -20) or ball.ycor() < -(SCREEN_HEIGHT/2 -20):
        ball.bounce_y()
    #detect when paddle misses
    if ball.xcor() > (SCREEN_WIDTH/2 -20):#paddleDx misses
        ball.reset_position()
        scoreboard.increase_score(isLeftPlayer=True)
    if ball.xcor() < -(SCREEN_WIDTH/2 -20):#paddleSx misses
        ball.reset_position()
        scoreboard.increase_score(isLeftPlayer=False)
    #detect collision with paddle
    if ball.distance(paddleSx) < 50 and ball.xcor() <= -330 or ball.distance(paddleDx) < 50 and ball.xcor() >= 330:
        ball.bounce_x()
        # screen.update()
        # ball.move()


screen.exitonclick()