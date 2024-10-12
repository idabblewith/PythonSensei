from days.day_086.files.helpers import *


def day_086():
    title("BREAKOUT")
    import turtle
    import time
    import random

    # Set up the screen
    window = turtle.Screen()
    window.title("Breakout")
    window.bgcolor("black")
    window.setup(width=600, height=600)
    window.tracer(0)  # Turns off screen updates

    # Create the paddle
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -250)

    # Create the ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.15
    ball.dy = -0.15

    # Create bricks
    bricks = []
    colors = ["red", "orange", "yellow", "green", "blue"]
    for i in range(5):
        new_brick = turtle.Turtle()
        new_brick.speed(0)
        new_brick.shape("square")
        new_brick.color(colors[i])
        new_brick.penup()
        new_brick.goto(-250, 200 - i * 24)
        bricks.append(new_brick)

    # Create a function to move the paddle left
    def move_left():
        x = paddle.xcor()
        if x > -250:
            paddle.setx(x - 20)

    # Create a function to move the paddle right
    def move_right():
        x = paddle.xcor()
        if x < 240:
            paddle.setx(x + 20)

    # Keyboard bindings
    window.listen()
    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")

    # Main game loop
    while True:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Boundary checking
        if ball.xcor() > 290:
            ball.setx(290)
            ball.dx *= -1
        if ball.xcor() < -290:
            ball.setx(-290)
            ball.dx *= -1
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        # Paddle and ball collisions
        if (
            ball.ycor() < -240
            and ball.ycor() > -250
            and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50)
        ):
            ball.sety(-240)
            ball.dy *= -1

        # Ball and brick collisions
        for brick in bricks:
            if ball.distance(brick) < 20:
                brick.goto(1000, 1000)  # Move the brick off screen
                bricks.remove(brick)
                ball.dy *= -1

        # Check if all bricks are destroyed
        if not bricks:
            window.clear()
            message = turtle.Turtle()
            message.speed(0)
            message.color("black")
            message.penup()
            message.hideturtle()
            message.goto(0, 0)
            message.write("You win!", align="center", font=("Courier", 24, "normal"))
            break

        # Game over if ball goes below the paddle
        if ball.ycor() < -290:
            window.clear()
            message = turtle.Turtle()
            message.speed(0)
            message.color("black")
            message.penup()
            message.hideturtle()
            message.goto(0, 0)
            message.write("Game Over", align="center", font=("Courier", 24, "normal"))

            break

        # Frame Delay
        # time.sleep(0.001)

    # Delay to show game over screen
    time.sleep(3)
    window.bye()
