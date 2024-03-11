from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.teleport(x_pos, y_pos)

    def paddle_up(self):
        self.forward(40)

    def paddle_down(self):
        self.backward(40)