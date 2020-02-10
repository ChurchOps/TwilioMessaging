# /usr/bin/env python
import os
import json
from six.moves.urllib.request import urlopen
from flask import Flask, request, render_template, flash, jsonify, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
from twilio.twiml.messaging_response import MessagingResponse
from app.forms import MessageForm, ContactForm, TagForm
from app.models import Contact, ContactTag, Tag
from app.send_sms import send_message
from app.oauth import AuthError, get_token_auth_header, requires_auth, requires_scope 
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

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)

# This needs authentication
@app.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)

# This needs authorization
@app.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private_scoped():
    if requires_scope("read:messages"):
        response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)


@app.route("/create/contact", methods=['GET', 'POST'])
def create_contact():
    """
    Handles Creating New Contacts
    """
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(FirstName=form.first_name,
                          Lastname=form.last_name,
                          Email=form.email,
                          Phone=form.phone)
        db.session.add(contact)
        db.session.commit()
        flash('Created Contact: {contact.__repr__()}')

    return render_template('contact.html',
                           form=form)



    return render_template('contact.html',
                           form=form)

if __name__ == "__main__":
    app.run(debug=True)
