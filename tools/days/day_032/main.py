# Copyright (c) 2024 Jarid Prince

from days.day_032.files.helpers import *


def day_032():
	title("BIRTHDAY WISHER")
	now = dt.datetime.now()
	today = str(now.date())
	nls("Reading Birthday CSV")
	a = pandas.read_csv("./tools/days/day_032/files/birthdays.csv")
	b = a.to_dict(orient="records")
	c = []
	for person in b:
		nls(f"Checking {person['name']}...")
		person["day"] = str(person["day"])
		person["month"] = str(person["month"])
		if len(person["day"]) == 1:
			person["day"] = "0" + person["day"]
		if len(person["month"]) == 1:
			person["month"] = "0" + person["month"]
		birthday = f'{person["year"]}-{person["month"]}-{person["day"]}'
		birthday_month_day = f'{person["month"]}-{person["day"]}'
		today_month_day = now.strftime("%m-%d")  # Extracting only month and day
		nls(f'BDAY: {birthday}')
		nls(f'TODAY: {today}')
		if birthday_month_day == today_month_day:
			nls(f"{person['name']}'s birthday today. Sending Email to {person["email"]}... ")
			num = random.randint(1, 3)
			file_path = f"./tools/days/day_032/files/letter_templates/letter_{num}.txt"
			with open(file_path) as bday_msg_file:
				contents = bday_msg_file.read()
				bday_msg = contents.replace("[NAME]", person["name"])
			load_dotenv()
			my_email = os.getenv("SENDER_EMAIL")
			# password = os.getenv("SENDER_EMAIL_PASSWORD")
			google_app_password = os.getenv("GOOGLE_APP_PASSWORD")

			with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
				conn.starttls()
				# conn.login(user=my_email, password=password)
				conn.login(user=my_email, password=google_app_password)

				conn.sendmail(
					from_addr=my_email,
					to_addrs=person["email"],
					msg=f"Subject: Happy Birthday!!\n\n{bday_msg}",
				)
