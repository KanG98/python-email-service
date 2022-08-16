import os 
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
mail= Mail(app)

email = 'yankang198.dev@gmail.com'
password = os.getenv('EMAIL_PASSWORD')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['TESTING'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('hi', sender = email, recipients = ['yankang198@gmail.com'])
   msg.body = "Hello hi message sent from Flask-Mail"
   msg.html = "<b>hihi</b>"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)

