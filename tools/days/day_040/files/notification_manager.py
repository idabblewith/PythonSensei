from days.day_040.files.helpers import *

with open('./tools/secrets/twilio_id.secret') as idf:
    TWILIO_SID = idf.read()
with open('./tools/secrets/twilio_token.secret') as tokf:
    TWILIO_AUTH_TOKEN = tokf.read()
with open('./tools/secrets/twilio_num.secret') as twin:
    TWILIO_VIRTUAL_NUMBER = twin.read()
with open('./tools/secrets/my_num.secret') as myn:
    TWILIO_VERIFIED_NUMBER = myn.read()
with open('./tools/secrets/email.secret') as emailf:
    email = emailf.read()
with open('./tools/secrets/email_password.secret') as passf:
    password = passf.read()

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

    def send_emails(self, message, person):
        with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
            conn.starttls()
            conn.login(user=email, password=password)
            conn.sendmail(
                from_addr=email, 
                to_addrs=person,
                msg=message)
