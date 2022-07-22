from days.day_031.files.helpers import *

def day_031():
	title("FLASH CARDS")
	try:
		data = pandas.read_csv("./tools/days/day_031/files/words_to_learn.csv")    
	except FileNotFoundError:
		unaltered_data = pandas.read_csv("./tools/days/day_031/files/french_words.csv")
		to_learn = unaltered_data.to_dict(orient='records')
	else:    
		to_learn = data.to_dict(orient="records")

	def check_remove():
		global fc_current_card
		to_learn.remove(fc_current_card)
		data = pandas.DataFrame(to_learn)
		data.to_csv("./tools/days/day_031/files/words_to_learn.csv", index=False)
		loop()
		# button_clicked = True
		# next_card(fc_flip_timer)

	def cross_redo():
		# global fc_current_card
		# print(fc_current_card)
		loop()

	# button_clicked = False
	window = Tk()
	window.title("Flashcard App")
	window.lift()
	window.attributes("-topmost", True)
	window.after_idle(window.attributes, '-topmost', False)
	window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
	
	card_front_img = PhotoImage(file="./tools/days/day_031/files/card_front.png")
	card_back_img = PhotoImage(file='./tools/days/day_031/files/card_back.png')
	canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
	card_bg = canvas.create_image(400,263, image=card_front_img)
	card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
	card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
	canvas.grid(row=0,column=0, columnspan=2)

	def center_window(width=900, height=800):
		screen_width = window.winfo_screenwidth()
		screen_height = window.winfo_screenheight()
		x = (screen_width/2) - (width/2)    
		y = (screen_height/2) - (height/2)
		window.geometry('%dx%d+%d+%d' % (width, height, x, y))
	center_window() 

	def set_current_card():
		global fc_current_card
		fc_current_card = random.choice(to_learn)
		canvas.itemconfig(card_title, text="French", fill="black")
		canvas.itemconfig(card_word, text=fc_current_card["French"], fill="black")
		canvas.itemconfig(card_bg, image=card_front_img)
		return fc_current_card

	def next_card():
		global fc_flip_timer
		global fc_current_card
		window.after_cancel(fc_flip_timer)
		fc_current_card = set_current_card()
		return fc_current_card


	dont_know_img = PhotoImage(file="./tools/days/day_031/files/wrong.png")
	dont_know_btn = Button(image=dont_know_img, highlightthickness=0, borderwidth=0,command=cross_redo)
	dont_know_btn.grid(row=1, column=0)

	know_img = PhotoImage(file="./tools/days/day_031/files/right.png")
	know_btn = Button(image=know_img, highlightthickness=0, borderwidth=0, command=check_remove)
	know_btn.grid(row=1, column=1)



	def set_flip_timer():
		# global fc_current_card
		global fc_flip_timer
		fc_flip_timer = window.after(4000, flip_card)
		return fc_flip_timer

	def flip_card():
		global fc_current_card
		canvas.itemconfig(card_title, text="English", fill="white")
		canvas.itemconfig(card_word, text=fc_current_card["English"], fill="white")
		canvas.itemconfig(card_bg, image=card_back_img)

	def loop():
		global fc_flip_timer
		window.after_cancel(fc_flip_timer)
		global fc_current_card
		fc_current_card = next_card()
		fc_flip_timer = set_flip_timer()
		return fc_current_card, fc_flip_timer

	global fc_current_card 
	fc_current_card = set_current_card()
	global fc_flip_timer 
	fc_flip_timer = set_flip_timer()
	fc_current_card, fc_flip_timer = loop()

	# window.after(8000, func=lambda:cross_redo(fc_flip_timer, fc_current_card))
	# window.after(6000, func=lambda: loop(fc_flip_timer))
		
	window.mainloop()

		