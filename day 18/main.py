import turtle
import random
import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
screen = Screen()  # IMPORTANT
screen.title("My Turtle App")

timmy = Turtle()
timmy.speed(5)
timmy.pensize(10)
# Square
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.penup()
# timmy.setpos(-400,-350)
# timmy.pendown()
# print(timmy.pos())
# for _ in range(40):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colours = [
    "medium turquoise",
    "light sea green",
    "cadet blue",
    "steel blue",
    "cornflower blue",
    "slate blue",
    "medium purple",
    "dark salmon",
    "indian red",
    "rosy brown",
    "khaki",
    "dark khaki",
    "wheat",
    "tan",
]

# def draw(sides):
#     angle = 360/sides
#     timmy.color(random.choice(colours))
#     for side in range(sides):
#         timmy.right(angle)
#         timmy.forward(100)

# for _ in range(3,11):
#     draw(_)


# angle = [0,90,180,270]
#
# for _ in range(random.randint(100,200)):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(angle))


# # Spirograph
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     c  = (r,g,b)
#     return c
#
# turtle.colormode(255)
#
# # def spir(size):
# #     for _ in range(int(360/size)):
# #         timmy.pencolor(random_color())
# #         timmy.circle(100)
# #         current_heading = timmy.heading()
# #         timmy.setheading(current_heading + size)
# #
# # spir(5)


# colors = colorgram.extract('image.jpg', 10)
# first_color = colors[0]
# rgb = first_color.rgb.r
# print(rgb)
# extracted = []
#
# for i in range(10):
#     r, g, b = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
#     extracted.append((r, g, b))
# print(extracted)


extracted = [ (231, 236, 243), (229, 238, 232),
             (39, 104, 168), (219, 157, 94),(230, 207, 118), (132, 85, 42),
             (221, 126, 149), (132, 168, 203)]
initial = -250
timmy.up()
timmy.hideturtle()
for rows in range(10):
    timmy.goto(-300,initial)
    for i in range(10):
        timmy.pencolor(random.choice(extracted))
        timmy.dot(20)
        timmy.forward(50)
    initial += 50

screen.exitonclick()  # IMPORTANT
