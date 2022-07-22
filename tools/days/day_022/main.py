# Copyright (c) 2022 Jarid Prince

from days.day_022.files.helpers import *
from days.day_022.files.paddle import Paddle
from days.day_022.files.score import Score
from days.day_022.files.ball import Ball

def day_022():
	title("PONG")
	screen = Screen()
	screen.bgcolor("black")
	screen.title("Pong")
	screen.setup(800,600)
	rootwindow = screen.getcanvas().winfo_toplevel()
	rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
	rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
	screen.tracer(0)

	l_paddle = Paddle((-350, 0))
	r_paddle = Paddle((350, 0))
	ball = Ball()
	score = Score()

	screen.listen()
	screen.onkeypress(l_paddle.go_up, "w")
	screen.onkeypress(l_paddle.go_down, "s")
	screen.onkeypress(r_paddle.go_up, "Up")
	screen.onkeypress(r_paddle.go_down, "Down")

	gameon = True

	while gameon:
		time.sleep(ball.move_speed)
		screen.update()
		ball.move()

		if ball.ycor() > 280 or ball.ycor() < -280:
			ball.bounce("y")

		if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
			ball.bounce("x")

		if ball.xcor() > 380:
			ball.reset_pos()
			score.point("left")
		if ball.xcor() < -380:
			ball.reset_pos()
			score.point("right")