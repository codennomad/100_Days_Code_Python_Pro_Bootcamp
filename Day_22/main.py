from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_pdd = Paddle((350, 0))
l_pdd = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Configurar eventos de teclado
screen.listen()

# Teclas para raquete direita
screen.onkeypress(r_pdd.start_up, "Up")
screen.onkeypress(r_pdd.start_down, "Down")
screen.onkeyrelease(r_pdd.stop, "Up")
screen.onkeyrelease(r_pdd.stop, "Down")

# Teclas para raquete esquerda
screen.onkeypress(l_pdd.start_up, "w")
screen.onkeypress(l_pdd.start_down, "s")
screen.onkeyrelease(l_pdd.stop, "w")
screen.onkeyrelease(l_pdd.stop, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    
    # Atualizar posição das raquetes
    
    r_pdd.update()
    l_pdd.update()
    
    screen.update()
    ball.move()
    
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with right paddle
    if ball.distance(r_pdd) < 50 and 320 < ball.xcor() < 350:
        ball.bounce_x(r_pdd, ball.ycor())
        
    # Detect collision with left paddle
    if ball.distance(l_pdd) < 50 and -350 < ball.xcor() < -320:
        ball.bounce_x(l_pdd, ball.ycor())
    
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()