import turtle
import time

# Настройка экрана
win = turtle.Screen()
win.title("Pong by YourName")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Ракетка A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Ракетка B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Мяч (ускоренный)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5  # Ускоренный мяч
ball.dy = 1.5

# Счет
score_a = 0
score_b = 0

# Пишем счет
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player А: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Переменные для управления движением
moving_up_a = False
moving_down_a = False
moving_up_b = False
moving_down_b = False

# Функции для управления игроком A
def start_move_a_up():
    global moving_up_a
    moving_up_a = True

def stop_move_a_up():
    global moving_up_a
    moving_up_a = False

def start_move_a_down():
    global moving_down_a
    moving_down_a = True

def stop_move_a_down():
    global moving_down_a
    moving_down_a = False

# Функции для управления игроком B
def start_move_b_up():
    global moving_up_b
    moving_up_b = True

def stop_move_b_up():
    global moving_up_b
    moving_up_b = False

def start_move_b_down():
    global moving_down_b
    moving_down_b = True

def stop_move_b_down():
    global moving_down_b
    moving_down_b = False

# Привязываем клавиши к функциям
win.listen()
win.onkeypress(start_move_a_up, "w")
win.onkeyrelease(stop_move_a_up, "w")
win.onkeypress(start_move_a_down, "s")
win.onkeyrelease(stop_move_a_down, "s")

win.onkeypress(start_move_b_up, "Up")
win.onkeyrelease(stop_move_b_up, "Up")
win.onkeypress(start_move_b_down, "Down")
win.onkeyrelease(stop_move_b_down, "Down")

# Основной игровой цикл
while True:
    win.update()

    # Движение ракеток при удерживании клавиш
    # Ракетка A
    if moving_up_a and paddle_a.ycor() < 250:
        y = paddle_a.ycor()
        y += 15  
        paddle_a.sety(y)
    if moving_down_a and paddle_a.ycor() > -250:
        y = paddle_a.ycor()
        y -= 15
        paddle_a.sety(y)
    
    # Ракетка B
    if moving_up_b and paddle_b.ycor() < 250:
        y = paddle_b.ycor()
        y += 15
        paddle_b.sety(y)
    if moving_down_b and paddle_b.ycor() > -250:
        y = paddle_b.ycor()
        y -= 15
        paddle_b.sety(y)

    # Движение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Проверка столкновения с верхней/нижней границей
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Проверка выхода за правую границу (счет игрока A)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Проверка выхода за левую границу (счет игрока B)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Отскок от ракеток
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1.1  

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1.1

    time.sleep(0.01)
