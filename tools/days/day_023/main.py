from days.day_023.files.helpers import *
from days.day_023.files.player import Player
from days.day_023.files.car_manager import CarManager
from days.day_023.files.scoreboard import Scoreboard
def day_023():
	title("TURTLE CROSSING CAPSTONE")
	screen = Screen()
	screen.setup(width=600, height=600)
	screen.tracer(0)

	player = Player()
	car = CarManager()
	score = Scoreboard()

	screen.listen()
	screen.onkeypress(player.move, "w")
	gameon = True
	while gameon:
		time.sleep(0.1)
		car.spawn()
		car.drive()
		screen.update()
		for item in car.cars:
			if player.distance(item) <= 25:
				print("you dead")
				score.game_over()
				gameon = False

		if player.finish() == True:
			score.update()
			player.back_to_start()
			car.level_up()


	screen.clear()
	screen.bye()