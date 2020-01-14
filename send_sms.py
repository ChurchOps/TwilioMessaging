# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv


def send_message(message):
    load_dotenv(verbose=True)

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_=os.getenv('FROM_NUMBER'),
                        to=os.getenv('TO_NUMBER')
                    )

    print(message.sid)

if __name__ == '__main__':
    send_message('HelloWorld')
