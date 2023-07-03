import os
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
EXAMPLE_PHOTO_URL = os.environ.get('EXAMPLE_PHOTO_URL')
TO_PHONE_NUMBER = os.environ.get('TO_PHONE_NUMBER')
FROM_PHONE_NUMBER = os.environ.get('FROM_PHONE_NUMBER')

# Your Account SID from twilio.com/console
account_sid = TWILIO_ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token = TWILIO_AUTH_TOKEN
photo_url = EXAMPLE_PHOTO_URL

client = Client(account_sid, auth_token)
message = client.messages.create(
            to=TO_PHONE_NUMBER, 
            from_=FROM_PHONE_NUMBER,
            body="John wants to gather with you, again!")
            # media_url=photo_url)

print(message.sid)
