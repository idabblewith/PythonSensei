from days.day_039.files.helpers import *

with open('./tools/secrets/twilio_id.secret') as idf:
    TWILIO_SID = idf.read()
with open('./tools/secrets/twilio_token.secret') as tokf:
    TWILIO_AUTH_TOKEN = tokf.read()
with open('./tools/secrets/twilio_num.secret') as twin:
    TWILIO_VIRTUAL_NUMBER = twin.read()
with open('./tools/secrets/my_num.secret') as myn:
    TWILIO_VERIFIED_NUMBER = myn.read()


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
