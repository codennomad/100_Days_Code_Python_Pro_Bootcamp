from turtle import Turtle, Screen

t = Turtle()

for _ in range(4):
    for _ in range(20):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(5)
    t.left(90)
    
screen = Screen()
screen.exitonclick()