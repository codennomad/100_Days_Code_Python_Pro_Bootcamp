from turtle import Turtle

class State_write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_data = data[data.state == ans]