from days.day_039.files.helpers import *


class NotificationManager:

    def __init__(self):
        load_dotenv()
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
