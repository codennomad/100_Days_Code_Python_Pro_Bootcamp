from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.bgcolor("black")

colours = ["#800080", "#8B008B", "#9932CC", "#9400D3", "#BA55D3","#DA70D6", "#D8BFD8", "#E6E6FA", "#DDA0DD", "#C71585"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.left(angle)
        
for shape_side_n in range(3, 11):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)
# [(t.color(random.choice(colours)), draw_shape(shape_side_n)) for shape_side_n in range(3, 11)]