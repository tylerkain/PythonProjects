from turtle import Turtle, Screen
import random
import heroes as heroes

name = heroes.gen()
tim = Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 15):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
