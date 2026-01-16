import tkinter
from turtle import Turtle,Screen


tim = Turtle()
screen = Screen()

def front():
    tim.forward(10)

def back():
    tim.back(10)

def right():
    tim.right(10)

def left():
    tim.left(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(front,'w')
screen.onkey(back,'s')
screen.onkey(right,'d')
screen.onkey(left,'a')
screen.onkey(clear,'c')
screen.exitonclick()
