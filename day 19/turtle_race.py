import random
import tkinter
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width = 500,height = 400)

colors =['red','blue','yellow','green','orange','pink']
turtles = []
# 6 turtles
x = -230
y = -165

guess = screen.textinput(title = "Bet for turtle",prompt= "Guess the turtle will win?")

for col in colors:
    trt = Turtle(shape = 'turtle')
    trt.color(col)
    trt.penup()
    trt.goto(x,y)
    y += 65
    turtles.append(trt)

# Race
finished = False
winner = 'trt'
while not finished:
    for trt in turtles:
        trt.forward(random.randint(1,5))
        if trt.pos()[0] >= 230:
            finished = True
            winner = trt.color()
            break


if winner[0] == guess.lower():
    print('You won the winner is ',winner[0],'!!')
else:
    print('You lost the winner is ',winner[0],'!!')

screen.exitonclick()
