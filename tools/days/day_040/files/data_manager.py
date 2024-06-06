from days.day_040.files.helpers import *


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.SHEETY_FLIGHT_ENDPOINT = os.getenv("SHEETY_FLIGHT_ENDPOINT")
        self.SHEETY_FLIGHT_ENDPOINT_2 = os.getenv("SHEETY_FLIGHT_ENDPOINT_2")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_FLIGHT_ENDPOINT)
        data = response.json()
        try:
            self.destination_data = data["prices"]
            return self.destination_data
        except:
            nls(
                f"{bcolors.WARNING}Sheety API monthly quota met, try again next month.{bcolors.ENDC}"
            )
            sys.exit()

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self.SHEETY_FLIGHT_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)

    def get_email_list(self):
        user_data = requests.get(url=self.SHEETY_FLIGHT_ENDPOINT_2)
        list = user_data.json()
        return list
