import turtle as turtle_module
import random

rows = 10
columns = 10

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
              (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
              (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
              (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
              (151, 206, 220)]


def go_home():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)


def draw_dot():
    color = random.choice(color_list)
    tim.pendown()
    tim.dot(20, color)
    return


def move(direction):
    tim.penup()
    if direction == "right":
        tim.setheading(0)
    elif direction == "left":
        tim.setheading(180)
    elif direction == "up":
        tim.setheading(90)
    elif direction == "down":
        tim.setheading(270)
    tim.forward(50)


go_home()
for y in range(rows):
    for x in range(columns):
        draw_dot()
        if y % 2 == 0:
            move("right")
        else:
            move("left")
    draw_dot()
    move("up")

screen = turtle_module.Screen()
screen.exitonclick()
