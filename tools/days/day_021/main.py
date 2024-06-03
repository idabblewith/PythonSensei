# Copyright (c) 2024 Jarid Prince

from days.day_021.files.helpers import *
from days.day_021.files.food import Food
from days.day_021.files.score import Score
from days.day_021.files.snake import Snake


def day_021():
    title("SNAKE GAME P2")
    screen = Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    screen.colormode(255)
    screen.title("Snake Game")
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    rootwindow.call("wm", "attributes", ".", "-topmost", "0")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")

    gameon = True
    while gameon:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            print("nom nom nom")
            food.refresh()
            snake.extend()
            score.updatescore()

        if (
            snake.head.xcor() > 380
            or snake.head.xcor() < -380
            or snake.head.ycor() > 380
            or snake.head.ycor() < -380
        ):
            gameon = False

        for segment in snake.snake_seg[1:]:
            if snake.head.distance(segment) < 10:
                gameon = False

    if gameon == False:
        score.game_over()
    screen.clear()
    screen.bye()
