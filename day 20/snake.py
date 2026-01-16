from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.seg = []
        self.tail_x = 0
        self.tail_y = 0
        for _ in range(3):
            self.add_snake()
        self.head = self.seg[0]

    def add_snake(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.tail_x,self.tail_y)
        self.seg.append(new_turtle)
        self.tail_x = new_turtle.xcor()-20
        self.tail_y = new_turtle.ycor()


    def move(self):
        for i in range(len(self.seg)-1,0,-1):
            self.seg[i].goto(self.seg[i-1].xcor(),self.seg[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)