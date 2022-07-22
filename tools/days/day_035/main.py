from days.day_035.files.helpers import *

def day_035():
    title("RAIN ALERT")
    with open("./tools/secrets/open_weather_api.secret") as api_file:
        api_key = api_file.read()
    with open("./tools/secrets/twilio_id.secret") as twid:
        account_sid = twid.read()
    with open("./tools/secrets/twilio_token.secret") as twoken:
        auth_token = twoken.read()
    with open("./tools/secrets/twilio_num.secret") as twinum:
        twilio_num = twinum.read()
    with open("./tools/secrets/my_num.secret") as my_numf:
        my_num = my_numf.read()

    params = {
        "lat":-31.9333,
        "lon":115.8333,
        "excludes":"alerts,daily,minutely,current",
        "appid":api_key
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
    response.raise_for_status()
    data = response.json()
    will_rain = False
    next_12 = data["hourly"][:12]
    for hour in next_12:
        weather_code = hour['weather'][0]["id"]
        if weather_code < 700: brelly = True
    if will_rain:
        client = Client(account_sid,auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today. Bring an umbrella.",
                from_=twilio_num,
                to=my_num
            )
        print(message.status)
