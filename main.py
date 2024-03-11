from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "i")
screen.onkey(l_paddle.paddle_down, "k")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect paddle collision
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_back()
    
    # Detect right out of bounds
    if ball.xcor() > 380:
        scoreboard.increase_lscore()
        ball.reset_position()

    # Detect left out of bounds
    if ball.xcor() < -380:
        scoreboard.increase_rscore()
        ball.reset_position()

screen.exitonclick()