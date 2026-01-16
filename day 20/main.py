import time
from turtle import Turtle,Screen
import tkinter as tk
from snake import Snake
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake body
snake = Snake()
screen.update()
game_on = True
screen.listen()
border = 300
while game_on:
    screen.update()
    time.sleep(0.1)

    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    snake.move()

    # Wall Logic
    if snake.head.xcor() >= 300 or snake.head.ycor() <= -300\
            or snake.head.xcor() <= -300 or snake.head.ycor() >= 300:
        game_on = False
        print('You lose border touched')



screen.exitonclick()