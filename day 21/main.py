import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Snake body
snake = Snake()
food = Food()
sb = Scoreboard()
screen.update()

game_on = True
screen.listen()
border = 300
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

    # Tail logic
    for segment in snake.seg[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            sb.game_over()
            break

    # Wall Logic
    if snake.head.xcor() >= 300 or snake.head.ycor() <= -300\
            or snake.head.xcor() <= -300 or snake.head.ycor() >= 300:
        game_on = False
        print('You lose border touched')
        sb.game_over()

    # Food and snake logic
    if food.distance(snake.head) < 15:
        print('nom nom nom')
        sb.increase_score()
        snake.add_snake()
        food.change_pos()



screen.exitonclick()