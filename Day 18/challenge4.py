from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
t.pensize(15)
t.speed(0)

# colours = ["#800080", "#8B008B", "#9932CC", "#9400D3", "#BA55D3","#DA70D6", "#D8BFD8", "#E6E6FA", "#DDA0DD", "#C71585"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for _ in range(600):
    t.forward(30)
    t.color(random_color()) #t.color(random.choice(colours))
    t.setheading(random.choice(directions))
    

# [(t.color(random.choice(colours)), t.forward(30), t.setheading(random.choice(directions))) for _ in range(600)]