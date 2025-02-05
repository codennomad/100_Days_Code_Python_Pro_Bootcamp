import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(150):
    t.circle(i * 2)  # Círculos crescentes
    t.right(90)  # Rotaciona um pouco

turtle.done()
