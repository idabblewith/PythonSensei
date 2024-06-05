from days.day_039.files.helpers import *


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.SHEETY_FLIGHT_ENDPOINT = os.getenv("SHEETY_FLIGHT_ENDPOINT")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.SHEETY_FLIGHT_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self.SHEETY_FLIGHT_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)
