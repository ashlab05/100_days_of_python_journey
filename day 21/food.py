from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.change_pos()
    def change_pos(self):
        x_cord = random.randint(-250, 250)
        y_cord = random.randint(-250, 250)
        self.goto( x_cord , y_cord )

