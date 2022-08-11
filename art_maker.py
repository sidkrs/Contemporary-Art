from turtle import Turtle
from turtle import Screen
import turtle as t
import random
t.colormode(255)


import colorgram
#colors from actual Damien Hirst Spot Painting
colors = [(239, 247, 244), (237, 241, 246), (249, 242, 246), (2, 13, 31), (52, 25, 17), (218, 128, 107), (11, 105, 159), (241, 213, 69), (149, 83, 40), (214, 87, 64), (164, 162, 32), (157, 7, 25), (156, 63, 102), (11, 63, 32), (96, 6, 20), (206, 74, 104), (12, 95, 56), (174, 135, 162), (1, 63, 145), (9, 173, 215), (156, 32, 22), (5, 212, 206), (10, 139, 85), (145, 227, 216), (122, 193, 149), (102, 219, 230), (221, 178, 216), (252, 197, 0), (117, 167, 190), (79, 135, 179), (30, 84, 91), (229, 174, 165), (184, 190, 203), (74, 70, 42)]

#put your name
hirst = Turtle()

#hide path
hirst.penup()

#hide cursor
hirst.hideturtle()

hirst.setposition(-245.13,-205.69)

def draw_line():
    for x in range(10):
        hirst.dot(20, random.choice(colors))
        hirst.speed("normal")
        hirst.forward(50)


for x in range(10):
    draw_line()
    hirst.speed("fastest")
    hirst.setheading(90)
    hirst.forward(50)
    hirst.setheading(180)
    hirst.forward(500)
    hirst.setheading(0)

numbers = random.randint(100000, 1000000)
value = "{:,}".format(numbers)

print(f"I think the painting is worth ${value}.")

screen = t.Screen()
screen.exitonclick()
