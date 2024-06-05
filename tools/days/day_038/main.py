# Copyright (c) 2024 Jarid Prince

from days.day_038.files.helpers import *


def day_038():
    title("NLP WORKOUT TRACKER")
    load_dotenv()
    NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
    NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
    SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
    SHEETY_WORKOUT_ENDPOINT = os.getenv("SHEETY_WORKOUT_ENDPOINT")

    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    sheet_endpoint = SHEETY_WORKOUT_ENDPOINT
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_KEY,
    }
    exercise = nli("What did you do?")

    params = {
        "query": exercise,
        "gender": "male",
        "weight_kg": "66",
        "height_cm": "166",
        "age": 31,
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

        bearer_headers = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"}
        sheet_response = requests.post(
            sheet_endpoint, json=sheet_inputs, headers=bearer_headers
        )

        nls("Natural Language Processing Complete!")
        print(f"{sheet_response.text}\nHead to {sheet_endpoint} to see exercises.")
