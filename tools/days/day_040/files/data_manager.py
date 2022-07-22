from days.day_040.files.helpers import *

with open('./tools/secrets/sheety_flight_api.secret') as sheetsss:
    SHEETY_ENDPOINT = sheetsss.read()
    # b3802b2b5a4106d64f4570a8f4e0915c



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        # https://docs.google.com/spreadsheets/d/17op5Iiq9Ws6lNw9obiPKpKFa-_tJu_Nhl47NYmEuq-Y/edit#gid=0
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        try:
            self.destination_data = data["prices"]
            return self.destination_data
        except:
            nls(f'{bcolors.WARNING}Sheety API monthly quota met, try again next month.{bcolors.ENDC}')
            sys.exit()

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_email_list(self):
        with open('./tools/secrets/sheety_flight_user.secret') as users:
            SHEETY_ENDPOINT2 = users.read()
        user_data = requests.get(url=SHEETY_ENDPOINT2)
        list = user_data.json()
        return list
