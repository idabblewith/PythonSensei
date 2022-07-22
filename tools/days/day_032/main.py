from days.day_032.files.helpers import *

def day_032():
	title("BIRTHDAY WISHER")
	now = dt.datetime.now()
	today = str(now.date())
	a = pandas.read_csv("./tools/days/day_032/files/birthdays.csv")
	b = a.to_dict(orient='records')
	c = []

	# for person in b:
	# 	person["day"] = str(person["day"])
	# 	person["month"] = str(person["month"])
	# 	if len(person["day"]) == 1:
	# 		person["day"] = "0" + person["day"]
	# 	if len(person["month"]) == 1:
	# 		person["month"] = "0" + person["month"]
	# 	birthday = f'{person["year"]}-{person["month"]}-{person["day"]}'
	# 	if birthday == today:
	# 		num = random.randint(1, 3)
	# 		file_path = f"./tools/days/day_032/files/letter_templates/letter_{num}.txt"
	# 		with open(file_path) as bday_msg_file:
	# 			contents = bday_msg_file.read()
	# 			bday_msg = contents.replace('[NAME]', person["name"])
	# 		with open("./tools/secrets/email_password.secret") as pass_file:
	# 			password = pass_file.read()
	# 		with open("./tools/secrets/email.secret") as email_file:
	# 			my_email = email_file.read()

	# 		with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
	# 			conn.starttls()
	# 			conn.login(user=my_email, password=password)
	# 			conn.sendmail(
	# 				from_addr=my_email, 
	# 				to_addrs=person["email"],
	# 				msg=f"Subject: Happy Birthday!!\n\n{bday_msg}")