# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from flask import Flask, request, render_template, flash
from twilio.twiml.messaging_response import MessagingResponse
from forms import MessageForm
from send_sms import send_message
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(verbose=True)
app.secret_key = os.getenv('SECRET')

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    home page for managing sms messages
    """
    form = MessageForm()
    if form.validate_on_submit():
        send_message(form.message)
        flash('Message Sent!')

    return render_template('index.html',
                           form=form)




@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
