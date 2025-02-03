import turtle
import random

# Configuração da tela
screen = turtle.Screen()
screen.title("Jogo de Tiro")
screen.bgcolor("black")

# Criando o jogador
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.setheading(90)  # Apontado para cima

# Criando o alvo
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(random.randint(-200, 200), random.randint(50, 200))

# Criando o tiro
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Função para atirar
def shoot():
    if not bullet.isvisible():  # Só atira se o tiro não estiver na tela
        bullet.goto(player.xcor(), player.ycor())
        bullet.showturtle()
        move_bullet()

# Movimento do tiro
def move_bullet():
    while bullet.ycor() < 250:
        bullet.sety(bullet.ycor() + 10)
        if bullet.distance(target) < 15:  # Se acertar o alvo
            target.goto(random.randint(-200, 200), random.randint(50, 200))  # Novo alvo
            bullet.hideturtle()
            return
    bullet.hideturtle()  # Se não acertar, esconde o tiro

# Movimentos do jogador
def move_left():
    player.setx(player.xcor() - 20)

def move_right():
    player.setx(player.xcor() + 20)

# Mapeamento das teclas
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot, "space")  # Atirar com espaço

screen.mainloop()
