from twilio.rest import Client
from config import Config

# Your Account SID from twilio.com/console
account_sid = Config.TWILIO_ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token  = Config.TWILIO_AUTH_TOKEN
photo_url = Config.EXAMPLE_PHOTO_URL

client = Client(account_sid, auth_token)

message = client.messages.create(
            to="+11234567890", 
            from_="+10987654321",
            body="John wants to gather with you, again!")
            # media_url=photo_url)

print(message.sid)
