from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import pickle

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

@app.route('/sms_capture')
def sms_capture():
    pickle.dump( request, open( "mock_requests/captured_request.p", "wb" ))
    with open('mock_requests/capture_requests.txt','w') as f:
        f.write(str(request.__dict__))

    return str(request.__dict__)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
