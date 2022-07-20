# Copyright (c) 2022 Jarid Prince

from days.day_007.files.helpers import *

def day_007():
	title("HANGMAN")
	nls(hangman_logo)
	lives = 6
	word = random.choice(hangman_words)
	display = ["_" for character in word]
	guesses = []
	

	def game_loop(guess):
		for position in range(0, len(word)):
			for letter in word[position]:
				if word[position] == guess:
					display[position] = letter

	end_of_game = False
	won = False

	while "_" in display and lives > 0:
		guess = nli("Guess a letter.").lower()
		cls()

		if guess in guesses:
			nls(hangman_stages[lives])
			nls(f"You have already tried that one!\nLives: {lives}")
		else:
			game_loop(guess)

			if guess in word:
				nls(hangman_stages[lives])
				nls(f"Well done! '{guess}' is in the word!\nLives: {lives}")
			else:
				lives-=1
				nls(hangman_stages[lives])
				nls(f"Nope! '{guess}' is not in the word! You lose a life!\nLives: {lives}")

			nls(f"You've already tried these:\n{guesses}")

			if lives == 0:
				end_of_game = True
				won = False

			guesses.append(guess)
			nls(display)

	if "_" not in display:
		won = True

	end_of_game = True

	if end_of_game: 
		if won:
			msg = "You win!"
		else:
			msg = f"You lose!\nThe words was {word}!"
		print("Game Over")
		nls(msg)