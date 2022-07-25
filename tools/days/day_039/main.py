# Copyright (c) 2022 Jarid Prince

from days.day_039.files.helpers import *
# from days.day_039.files.data_manager import DataManager
# from days.day_039.files.flight_search import FlightSearch
# from days.day_039.files.notification_manager import NotificationManager

def day_039():
	title("FLIGHT SCANNER")
	print("Day is being reconstructed")
	# data_manager = DataManager()
	# sheet_data = data_manager.get_destination_data()
	# flight_search = FlightSearch()
	# notification_manager = NotificationManager()

	# ORIGIN_CITY = "PER"

	# if sheet_data[0]["iataCode"] == "":
	# 	for row in sheet_data:
	# 		row["iataCode"] = flight_search.get_destination_code(row["city"])
	# 	data_manager.destination_data = sheet_data
	# 	data_manager.update_destination_codes()

	# tomorrow_base = dt.now() +timedelta(1)
	# tomorrow = tomorrow_base.strftime('%d/%m/%Y')
	# six_later_base = tomorrow_base + timedelta((6 * 30))
	# six_later = six_later_base.strftime('%d/%m/%Y')

	# for destination in sheet_data:
	# 	flight = flight_search.check_flights(
	# 		ORIGIN_CITY,
	# 		destination["iataCode"],
	# 		from_time=tomorrow,
	# 		to_time=six_later
	# 	)
	# 	if flight == None:
	# 		continue
	# 	elif flight.price < destination["lowestPrice"]:
	# 		notification_manager.send_sms(
	# 			message=f"Low price alert! Only AUD${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
	# 		)