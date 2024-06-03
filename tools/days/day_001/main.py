# Copyright (c) 2024 Jarid Prince

from misc import *


def day_001():
    title("Band Name Generator")
    city = nli("What's the name of the city you grew up in?")
    pet = nli("What's your pet's name?")
    bandname = city + pet
    nls(f"Your band name is: \n{bandname}")
