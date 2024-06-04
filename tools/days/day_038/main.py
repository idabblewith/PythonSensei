# Copyright (c) 2024 Jarid Prince

from days.day_038.files.helpers import *


def day_038():
    title("NLP WORKOUT TRACKER")
    with open("./tools/secrets/nutritionix_app.secret") as appf:
        APP_ID = appf.read()
    with open("./tools/secrets/nutritionix_api.secret") as api_file:
        API_KEY = api_file.read()
    with open("./tools/secrets/sheety_bearer.secret") as bearerf:
        BEARER_TOKEN = bearerf.read()

    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    sheet_endpoint = (
        "https://api.sheety.co/15ae3c416bf45dc7d700adaa6ce50555/myWorkouts/workouts"
    )
    # https://docs.google.com/spreadsheets/d/104GckXSrs7j34eY--r7GiK085zArnsjlyit8H9A2e1A/edit#gid=0

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    exercise = nli("What did you do?")

    params = {
        "query": exercise,
        "gender": "male",
        "weight_kg": "68",
        "height_cm": "166",
        "age": 27,
    }

    response = requests.post(url=exercise_endpoint, json=params, headers=headers)
    result = response.json()

    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    for exercise in result["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

        bearer_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        sheet_response = requests.post(
            sheet_endpoint, json=sheet_inputs, headers=bearer_headers
        )

        nls("Natural Language Processing Complete!")
        print(f"{sheet_response.text}\nHead to {sheet_endpoint} to see exercises.")
