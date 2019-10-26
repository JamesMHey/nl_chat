from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import pickle
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', "config.DevelopmentConfig"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    from models import Result
    return "Hello World!"


@app.route('/sms')
def hello_name():
    return str(request.__repr__)

@app.route('/sms_capture', methods=['GET', 'POST'])
def sms_capture():
    pickle.dump( request, open( "mock_requests/captured_request.p", "wb" ))
    with open('mock_requests/capture_requests.txt','w') as f:
        f.write(str(request.__dict__))
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
