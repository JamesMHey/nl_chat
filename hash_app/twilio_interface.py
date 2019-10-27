from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

class TwilioInterface:
    TEST_NUMBER = '+447854369726'
    def __init__(self):
        self.our_number = '+447479272367'
        
        try:
            self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
            self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        except KeyError:
            command = "source .env"
            os.system(command)
            self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
            self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

    def send_SMS(self, recieving_number, contents):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
                        .create(
                             body=contents,
                             from_ = self.our_number,
                             to = recieving_number)

if __name__ == "__main__":
    bot = TwilioInterface()
    from datetime import datetime
    bot.send_SMS(bot.TEST_NUMBER, 'Test text at {}'.format(datetime.now()))


