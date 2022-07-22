from days.day_040.files.helpers import requests,nls,nli
# https://replit.com/@jptokyo/flightclub#main.py

with open('./tools/secrets/sheety_flight_user.secret') as users:
    SHEETY_ENDPOINT2 = users.read()

nls("Welcome to the Flight Club.")
nls('We curate the best flight deals!')
first_name = nli('What is your first name? ').title()
last_name = nli('What is your last name? ').title()
while True:
    email = nli('What is your email? ').lower()
    email_verification = nli('Please, re-type your email: ').lower()
    if email == email_verification:
        break

users = {'user': dict(firstName=first_name, lastName=last_name, email=email)}
requests.post(url=SHEETY_ENDPOINT2, json=users)

print("You're in the club!")