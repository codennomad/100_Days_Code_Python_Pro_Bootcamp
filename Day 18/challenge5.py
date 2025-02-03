from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
# t.pensize(15)
t.speed(0)

# colours = ["#800080", "#8B008B", "#9932CC", "#9400D3", "#BA55D3","#DA70D6", "#D8BFD8", "#E6E6FA", "#DDA0DD", "#C71585"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spinrongraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
        
draw_spinrongraph(5)
screen.exitonclick()
