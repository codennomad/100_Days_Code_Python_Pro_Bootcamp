from turtle import Turtle
import math
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 7  # Velocidade base da bola
        self.max_speed = 15  # Velocidade máxima
        self.acceleration = 1.1  # Fator de aceleração após cada rebatida
        self.move_speed = 0.1  # Delay do jogo (diminui com a velocidade)
        self.reset_position()
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        # Reflexão na parede com pequena perda de energia
        self.y_move *= -0.95
        
    def bounce_x(self, paddle, hit_y):
        # Calcula o ponto de impacto relativo na raquete (-1 a 1)
        relative_hit = (hit_y - paddle.ycor()) / 50
        
        # Ângulo de reflexão baseado no ponto de impacto (-45 a +45 graus)
        bounce_angle = relative_hit * 45
        
        # Aumenta a velocidade após cada rebatida
        self.speed = min(self.speed * self.acceleration, self.max_speed)
        
        # Calcula nova direção baseada no ângulo
        direction = -1 if self.x_move > 0 else 1
        self.x_move = direction * self.speed * math.cos(math.radians(bounce_angle))
        self.y_move = self.speed * math.sin(math.radians(bounce_angle))
        
        # Acelera o jogo (diminui o delay)
        self.move_speed = max(0.03, self.move_speed * 0.9)
    
    def reset_position(self):
        self.goto(0, 0)
        self.speed = 7  # Reseta para a velocidade inicial
        self.move_speed = 0.1  # Reseta o delay do jogo
        
        # Escolhe um ângulo inicial aleatório (entre 30 e 60 graus)
        angle = random.uniform(30, 60)
        if random.random() < 0.5:  # 50% de chance de ir para cada lado
            angle = 180 - angle
            
        # Calcula os componentes de movimento baseados no ângulo
        self.x_move = self.speed * math.cos(math.radians(angle))
        self.y_move = self.speed * math.sin(math.radians(angle))