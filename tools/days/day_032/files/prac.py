import datetime as dt
import random
import smtplib

now = dt.datetime.now()
print(now)
array_of_quotes_2 = []
with open("./Other/Completed/n32/quotes.txt") as quotes_file:
        array_of_quotes = quotes_file.readlines()
        for i in array_of_quotes:
            i.strip()
            array_of_quotes_2.append(i)
quote = random.choice(array_of_quotes_2)

alldays = [0,1,2,3,4,5,6]
# if now.day in alldays and now.hour == 7 and now.minute == 30 and now.second == 0 and now.microsecond == 0:
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    my_email = "dmasamune.dokuganryuu@gmail.com"
    my_other_emails = ["dmasamune.dokuganryuu@yahoo.com"]
    with open("./Other/Completed/n32/password.secret") as pw:
        password = pw.read()

    connection.starttls()
    connection.login(user=my_email, password=password)
    for sendemail in my_other_emails:

        connection.sendmail(
            from_addr=my_email,
            to_addrs=sendemail,
            msg=f"Subject: Daily Quote\n\n{quote}"
        )