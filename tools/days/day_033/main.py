# Copyright (c) 2024 Jarid Prince

from days.day_033.files.helpers import *


MY_LAT = -31.981800
MY_LONG = 115.863708


# Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 8
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 8
    if sunrise >= 24:
        sunrise = sunrise - 24
    if sunset >= 24:
        sunset = sunset - 24

    now = dt.now()

    if now.hour >= sunset or now.hour <= sunrise:
        print(now)
        print(sunrise)
        print(sunset)
        return True
        # Its dark


def day_033():
    title("ISS TRACKER")
    nls(
        "Watching to see if ISS is overhead. Will check if should send email every minute."
    )
    load_dotenv()
    MY_EMAIL = os.getenv("SENDER_EMAIL")
    # password = os.getenv("SENDER_EMAIL_PASSWORD")
    MY_PASS = os.getenv("GOOGLE_APP_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    while True:
        if is_night() and iss_overhead():
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.send_message(
                    from_addr=MY_EMAIL,
                    to_addrs=RECEIVER_EMAIL,
                    msg="Subject: ISS Overhead!\n\n Look up! The ISS is above your location!",
                )
        else:
            nls("Didn't send an email for this minute. Sleeping for a minute...")
        time.sleep(60)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
