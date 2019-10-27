from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import pickle
from twilio.twiml.messaging_response import MessagingResponse
from twilio_interface import TwilioInterface
import requests, codecs, hashlib

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', "config.DevelopmentConfig"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    from models import Result
    return "Hello World!"



@app.route('/sms_capture', methods=['GET', 'POST'])
def sms_capture():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    from_n = request.values.get('From')
    from_n = get_hash(from_n)
    # Add a message
    resp.message("body {}. From {}".format(body, from_n))
    return str(resp)

@app.route('/sms_send', methods=['GET', 'POST'])
def sms_send():
    from models import HashPair

    body = request.values.get('content')
    uid = request.values.get('uid') 
    TI = TwilioInterface()




def send_message_on(uid, message_content):
    url = 'localhost:8000/incoming_sms'
    data = {'from': uid, 'content': content}
    resp = requests.post(url, data = data)
    # if resp is okay, mark in DB. 

def get_hash(phone_number):
    phone_number = phone_number+get_salt(phone_number)
    hs = hashlib.md5(phone_number.encode('utf-8')).hexdigest()
    b64 = codecs.encode(codecs.decode(hs, 'hex'), 'base64').decode()
    return b64

def get_salt(phone_number):
    return ''

def get_number_from_uid(uid): # Return phone number if exists (else false)
    pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
