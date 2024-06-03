# Copyright (c) 2024 Jarid Prince

from misc import title, nli, nls


def day_006():
    title("BMI CHECKER")
    height = float(nli("How tall are you in cm?"))
    weight = float(nli("How much do you weigh in kg?"))
    bmi = round(weight / (height / 100) ** 2, 2)
    if bmi < 18.5:
        weight_class = "underweight"
    elif bmi < 25:
        weight_class = "normal weight"
    elif bmi < 30:
        weight_class = "overweight"
    elif bmi < 35:
        weight_class = "obese"
    else:
        weight_class = "clinically obese"

    nls(f"Your BMI is {bmi}\nYou are {weight_class}")
