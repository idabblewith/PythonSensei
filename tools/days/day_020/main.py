# Copyright (c) 2024 Jarid Prince

from days.day_020.files.helpers import *
from days.day_020.files.food import Food
from days.day_020.files.score import Score
from days.day_020.files.snake import Snake


def day_020():
    title("SNAKE GAME P1")
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
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    gameon = True
    try:
        while gameon:
            screen.update()
            sleep_rate = 0.1
            time.sleep(sleep_rate)
            snake.move()

            if snake.head.distance(food) < 15:
                print("nom nom nom")
                food.refresh()
                food.updatescore()
            # print(f'{snake.head.xcor()},{snake.head.ycor()}')

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
        screen.clear()
        screen.bye()

    except Exception as e:
        print(e)
        while gameon:
            screen.update()
            sleep_rate = 0.1
            time.sleep(sleep_rate)
            snake.move()

            if snake.head.distance(food) < 15:
                print("nom nom nom")
                food.refresh()
                food.updatescore()
            if (
                snake.head.xcor() > 380
                or snake.head.xcor() < -380
                or snake.head.ycor() > 380
                or snake.head.ycor() < -380
            ):
                print(f"{snake.head.xcor()},{snake.head.ycor()}")
                gameon = False

            for segment in snake.snake_seg[1:]:
                if snake.head.distance(segment) < 10:
                    gameon = False
        screen.clear()
        screen.bye()
