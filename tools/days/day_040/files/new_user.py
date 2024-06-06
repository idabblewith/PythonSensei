from days.day_040.files.helpers import requests, nls, nli, os, load_dotenv

# https://replit.com/@idabblewith/flightclub#main.py

load_dotenv()
SHEETY_FLIGHT_ENDPOINT_2 = os.getenv("SHEETY_FLIGHT_ENDPOINT_2")

nls("Welcome to the Flight Club.")
nls("We curate the best flight deals!")
first_name = nli("What is your first name? ").title()
last_name = nli("What is your last name? ").title()
while True:
    email = nli("What is your email? ").lower()
    email_verification = nli("Please, re-type your email: ").lower()
    if email == email_verification:
        break

users = {"user": dict(firstName=first_name, lastName=last_name, email=email)}
requests.post(url=SHEETY_FLIGHT_ENDPOINT_2, json=users)

print("You're in the club!")
