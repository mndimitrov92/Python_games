import turtle

# Initialize the scrren
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Set the speed to the maximum possible
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Set the speed to the maximum possible
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Set the speed to the maximum possible
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # Set initial position
ball.dx = 4
ball.dy = 4

# Score text
pen = turtle.Turtle()
pen.speed(0)  # Animation speed
pen.color("yellow")
pen.penup()  # Hides the line
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score initialization
score_a = 0
score_b = 0


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()  # Listen to keyboard input
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom borders
    if ball.ycor() > 290:  # top part of the screen is 300px from the center - half ball height(10px)
        ball.sety(290)
        ball.dy *= -1  # Reverse the direction
    if ball.ycor() < -290:  # bottom part of the screen is -300px from the center - half ball height(10px)
        ball.sety(-290)
        ball.dy *= -1  # Reverse the direction

    # left and right borders
    if ball.xcor() > 390:  # pass the paddle
        ball.goto(0, 0)  # Place at the center
        ball.dx *= -1
        score_a += 1

    if ball.xcor() < -390:  # pass the paddle
        ball.goto(0, 0)  # Place at the center
        ball.dx *= -1
        score_b += 1

    # Paddle - ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (
            ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (
            ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Update the score
    pen.clear()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    window.update()
