import os
from twilio.rest import Client

# Set up TWILIO API for SMS
# Twilio SID, authentication token, phone number, and the Twilio phone number

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MY_DIGITS']
twilio_number = os.environ['TWILIO_DIGITS']
client = Client(account_sid, auth_token)

message = client.messages.create(
            body='Someone is home!',
            from_=twilio_number,
            to=my_number
        )
print(message.sid)