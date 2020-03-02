# /usr/bin/env python
import os
import json
from six.moves.urllib.request import urlopen
from flask import Flask, request, render_template, flash, jsonify, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
from twilio.twiml.messaging_response import MessagingResponse
from app import app
from app.forms import MessageForm, ContactForm
from app.send_sms import send_message
from app.etl import Uploader
from app.oauth import AuthError, get_token_auth_header, requires_auth, requires_scope 


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    home page for managing sms messages
    """
    message_form = MessageForm()
    if message_form.validate_on_submit():
        send_message(message_form.message)
        flash('Message Sent!')

    return render_template('index.html',
                           MessageForm=message_form)

@app.route('/upload', methods=['GET', 'POST'])
def upload_contacts():
    """
    upload contacts and tags page
    """
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        contact = [{"first_name":contact_form.first_name,"last_name":contact_form.last_name,
                    "Email":contact_form.Email, "Phone":contact_form.Phone}]
        u = Uploader(contact)
        u.upload_contacts()
        flash(f"created contact: {contact}")
        redirect
    return render_template('upload.html', ContactForm=contact_form)



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

if __name__ == "__main__":
    app.run(debug=True)
