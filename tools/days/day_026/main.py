from days.day_026.files.helpers import *

def day_026():
	title("NATO ALPHABET")
	natos = pandas.read_csv('./tools/days/day_026/files/nato_phonetic_alphabet.csv')
	phonetic_dict = {row.letter:row.code for (index, row) in natos.iterrows()}
	name = nli("Type your name: ").upper()
	result = [phonetic_dict[letter] for letter in name]
	nls(result)