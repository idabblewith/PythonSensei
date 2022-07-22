# Copyright (c) 2022 Jarid Prince

from days.day_027.files.helpers import *

def day_027():
	title("Kilometers to Miles")
	window = Tk()

	window.attributes('-topmost', True)
	window.update()
	window.attributes('-topmost', False)

	window.title("Kilometers to Miles")
	window.minsize(width=300,height=200)
	window.iconbitmap("./tools/days/day_027/files/icon.ico")

	km_label = Label(text="Enter KM Value:")
	km_label.grid(column=2, row=1, padx=10, pady=0)
	km = Entry(width=20)
	km.grid(column=2, row=2, padx=10, pady=10)
	miles = Label(text="Miles")
	miles.grid(column=2, row=3, padx=20,pady=2)

	def convertor_clicked():
		kilometers = round(float(km.get()),2)
		
		miles["text"] = f'{kilometers} KM is equal to {round(kilometers*0.621371, 2)} Miles'

	convert = Button(text="Convert", command=convertor_clicked)
	convert.grid(column=3, row=2,padx=3,pady=0)

	window.mainloop()