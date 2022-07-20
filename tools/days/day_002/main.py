# Copyright (c) 2022 Jarid Prince

from misc import *

def day_002():
    title("BILL SPLITTER")
    bill = float(nli("What's the bill total?"))
    people = int(nli("How many people are splitting?"))
    tip = int(nli("What's the percentage of the tip?\n0, 10, 12, 15?"))
    total_bill = (bill * (tip/100)) + bill
    pp = "{:.2f}".format(total_bill/people)
    nls(f"Total per person is: ${pp}")