from days.day_040.files.helpers import *
from days.day_040.files.flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
with open("./tools/secrets/tequila_api.secret") as teqf:
    TEQUILA_API_KEY = teqf.read()

class FlightSearch:
    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_names):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}


        for city in city_names:
            query = {"term": city, "location_types": "city"}

            # req = requests.Request('POST',location_endpoint,headers=headers,params=query)
            # prepared = req.prepare()
            # nls(f'{bcolors.OKCYAN}PREPARED:\n{prepared}{bcolors.ENDC}')

            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]

            self.city_codes.append(code)
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, max_stops=None):
        headers = {"apikey": TEQUILA_API_KEY}
        oneway = True
        if oneway == True:
            query = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time,
                "date_to": to_time,
                "flight_type": "oneway",
                "one_for_city": 1,
                "max_stopovers": 0 if max_stops == None else max_stops,
                "curr": "AUD",
            }
        else:    
            query = {
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time,
                "date_to": to_time,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0 if max_stops == None else int(max_stops),
                "curr": "AUD",
            }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        nls(f'{bcolors.OKCYAN}PREPARED:\n{response.json()}{bcolors.ENDC}')

        # pprint(response.text)
        
        try:
            data = response.json()["data"][0]
        except IndexError as e:
            nls(f'{bcolors.OKBLUE}{e}{bcolors.ENDC}')
            return None
        except Exception as e:
            nls(f'{bcolors.FAIL}{e}{bcolors.ENDC}')
            return None
        else:
            if oneway == True:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                )
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
            # nls(f'{bcolors.WARNING}{data["price"]}{bcolors.ENDC}')
            pprint(f'{data}')
            return flight_data