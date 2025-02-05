# import os
# import colorgram

# rgb_colors = []

# # Procurando o arquivo 'zhuo.jpg' em diferentes diretórios
# for root, dirs, files in os.walk('.'):
#     if 'zhuo.jpg' in files:
#         image_path = os.path.join(root, 'zhuo.jpg')
#         break
# else:
#     print("Erro: Não foi possível encontrar o arquivo 'zhuo.jpg'.")
#     exit()

# colors = colorgram.extract(image_path, 15)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

color_list = [
    (43, 26, 19), 
    (135, 88, 66), 
    (217, 136, 111), 
    (249, 233, 209), 
    (110, 42, 36), 
    (199, 92, 84), 
    (50, 28, 30), 
    (88, 67, 29), 
    (1, 3, 1), 
    (163, 128, 79), 
    (236, 214, 123), 
    (102, 42, 44), 
    (131, 62, 65), 
    (239, 161, 150), 
    (8, 8, 11)
]

t.speed(0)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
        
screen.exitonclick()
    