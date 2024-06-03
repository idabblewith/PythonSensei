# Copyright (c) 2024 Jarid Prince

from misc import nli, nls, title
import random, string


def day_005():
    title("PASSWORD GENERATOR")
    AVAIL_CHAR = [char for char in string.printable]
    NUMBER = AVAIL_CHAR[:10]
    ALPHA = AVAIL_CHAR[10:62]
    SYMBOL = AVAIL_CHAR[62:-6]
    numbers_amount = int(nli("How many numbers would you like in your password?")) + 1
    alphabet_amount = int(nli("How many letters would you like in your password?")) + 1
    symbols_amount = int(nli("How many symbols would you like in your password?")) + 1
    new_pass_array = []

    for each_number in range(1, numbers_amount):
        new_pass_array.append(random.choice(NUMBER))
    for each_letter in range(1, alphabet_amount):
        new_pass_array.append(random.choice(ALPHA))
    for each_symbol in range(1, symbols_amount):
        new_pass_array.append(random.choice(SYMBOL))

    random.shuffle(new_pass_array)
    new_pass = ""

    for character in new_pass_array:
        new_pass += character

    nls(f"Here is your new password: {new_pass}")
