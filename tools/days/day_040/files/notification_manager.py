from days.day_040.files.helpers import *


class NotificationManager:

    def __init__(self):
        load_dotenv()
        self.SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        self.GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
        self.TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_NUM = os.getenv("TWILIO_NUM")
        self.MY_PERSONAL_NUMBER = os.getenv("MY_PERSONAL_NUMBER")
        self.client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.TWILIO_NUM,
            to=self.MY_PERSONAL_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, person):
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=self.SENDER_EMAIL, password=self.GOOGLE_APP_PASSWORD)
            conn.sendmail(from_addr=self.SENDER_EMAIL, to_addrs=person, msg=message)
