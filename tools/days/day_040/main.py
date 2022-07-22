from days.day_040.files.helpers import *
# from days.day_040.files.data_manager import DataManager
# from days.day_040.files.flight_search import FlightSearch
# from days.day_040.files.notification_manager import NotificationManager

def day_040():
	title("FLIGHT CLUB")
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

	# cheap = []
	# for destination in sheet_data:
	# 	nls(f'{bcolors.HEADER}{destination["city"]}{bcolors.ENDC}')
	# 	flight = flight_search.check_flights(
	# 		ORIGIN_CITY,
	# 		destination["iataCode"],
	# 		from_time=tomorrow,
	# 		to_time=six_later
	# 	)

	# 	if flight == None:
	# 		nls(f'{bcolors.WARNING}No direct flights found for {destination["iataCode"]}.{bcolors.ENDC}')
	# 		stopover_flight = flight_search.check_flights(
	# 			ORIGIN_CITY,
	# 			destination["iataCode"],
	# 			from_time=tomorrow,
	# 			to_time=six_later,
	# 			max_stops=1
	# 		)
	# 		if stopover_flight == None:

	# 			nls(f'{bcolors.WARNING}No stopover flights found for {destination["iataCode"]}.{bcolors.ENDC}')
	# 		elif stopover_flight.price < destination["lowestPrice"]:
	# 			print(f'{bcolors.FAIL}"STOPOVER FLIGHT FOUND"{bcolors.ENDC}')
	# 			nls(f'{bcolors.OKGREEN}{stopover_flight.origin_city}-{destination["city"]} @ ${stopover_flight.price}\n{stopover_flight.out_date} via {stopover_flight.destination_city}{bcolors.ENDC}')
	# 			# stop_to_dest =

	# 			cheap.append(dict(fromCity=stopover_flight.origin_city, toCity=stopover_flight.destination_city, price=stopover_flight.price, fromDate=stopover_flight.out_date, toDate=stopover_flight.return_date, stops=stopover_flight.stop_overs, viaCity=stopover_flight.via_city))
	# 	elif flight.price < destination["lowestPrice"]:
	# 		nls(f'{bcolors.OKGREEN}{flight.origin_city}-{flight.destination_city} @ ${flight.price}\n{flight.out_date}{bcolors.ENDC}')

	# 		cheap.append(dict(fromCity=flight.origin_city, toCity=flight.destination_city, price=flight.price, fromDate=flight.out_date, toDate=flight.return_date ))
	# print(cheap)

	# email_list = data_manager.get_email_list()
	# # print(email_list)
	# # for user in email_list["users"]:
	# # 	message = ''
	# # 	for cheap_flight in cheap:
	# # 		if cheap_flight['stops']:
	# # 			message += f"\nLow price alert!\n{cheap_flight['fromCity']}-{cheap_flight['toCity']} | AUD${cheap_flight['price']}\n{cheap_flight['fromDate']}\nSTOPOVERS: {cheap_flight['stops']} via {cheap_flight['viaCity']}"
	# # 		else:	
	# # 			message += f"\nLow price alert!\n{cheap_flight['fromCity']}-{cheap_flight['toCity']} | AUD${cheap_flight['price']}\n{cheap_flight['fromDate']} to {cheap_flight['toDate']}\n"

	# # 	print(f'Sent below message to {user["email"]}:\n{message}')
	# 	# notification_manager.send_emails(message=message, person=user["email"])

	# 		# https://www.faredetective.com/farehistory/