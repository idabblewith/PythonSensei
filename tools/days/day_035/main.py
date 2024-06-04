# Copyright (c) 2024 Jarid Prince

from days.day_035.files.helpers import *


def day_035():
    title("RAIN ALERT")
    load_dotenv()
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_NUM = os.getenv("TWILIO_NUM")
    MY_PERSONAL_NUMBER = os.getenv("MY_PERSONAL_NUMBER")

    params = {
        "units": "metric",
        "lang": "en",
        "lat": -31.9333,
        "lon": 115.8333,
        "exclude": "alerts,daily,minutely,current",
        "appid": OPEN_WEATHER_API_KEY,
    }

    response = requests.get(
        # url="https://api.openweathermap.org/data/2.5/weather",
        # params=params,
        url="https://api.openweathermap.org/data/3.0/onecall",
        params=params,
    )
    response.raise_for_status()
    data = response.json()
    brelly = False
    next_12 = data["hourly"][:12]
    for hour in next_12:
        weather_code = hour["weather"][0]["id"]
        if weather_code < 700:
            brelly = True
    if brelly:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body="It's going to rain within the next 12H. Bring an umbrella.",
            from_=TWILIO_NUM,
            to=MY_PERSONAL_NUMBER,
        )
        print(message.status)
