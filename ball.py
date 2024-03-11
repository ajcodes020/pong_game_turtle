from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move_speed = 0.05
    
    def move(self):
        self.forward(10)

    def bounce(self):
        self.setheading(self.heading() * -1)

    def bounce_back(self):
        self.bounce()
        self.setheading(self.heading() + 180)
        self.move_speed *= .9
    
    def reset_position(self):
        self.teleport(0, 0)
        self.bounce_back()
        self.move_speed = 0.05