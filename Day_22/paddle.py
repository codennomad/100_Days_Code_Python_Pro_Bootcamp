from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.moving_up = False
        self.moving_down = False
        self.speed = 15
        
    def start_up(self):
        self.moving_up = True
        self.moving_down = False
        
    def start_down(self):
        self.moving_down = True
        self.moving_up = False
        
    def stop(self):
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_up and self.ycor() < 250:
            new_y = self.ycor() + self.speed
            self.goto(self.xcor(), new_y)
        elif self.moving_down and self.ycor() > -250:
            new_y = self.ycor() - self.speed
            self.goto(self.xcor(), new_y)