from flask import Flask, render_template, request, flash, redirect, url_for
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    msg = f"{request.form['w1']} : {request.form['m1']}\n" + \
          f"{request.form['w2']} : {request.form['m2']}\n" + \
          f"{request.form['w3']} : {request.form['m3']}\n" + \
          f"{request.form['w4']} : {request.form['m4']}\n" + \
          f"{request.form['w5']} : {request.form['m5']}\n" + \
          f"{request.form['w6']} : {request.form['m6']}\n" + \
          f"{request.form['w7']} : {request.form['m7']}\n"
    message = client.messages.create(
        to='+91' + request.form['mobile'],
        from_=TWILIO_PHONE_NUMBER,
        body="\n" + msg
    )
    if message.sid:
        flash('SUCCESSFULLY DELIVERED')
    else:
        flash('DELIVERY FAILED')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
