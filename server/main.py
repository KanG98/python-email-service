import os 
from flask import Flask, make_response
from mailing import Mailing, Message
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
   email = 'yankang198.dev@gmail.com'
   password = os.getenv('EMAIL_PASSWORD')
   mail= Mailing(app, email, password)


   msg = Message('hi', sender = email, recipients = ['yankang198@gmail.com'])
   # msg.body = "Helo hi message sent from Flask-Mail"
   msg.html = "<b>hihi</b>"

   # with app.open_resource("image.png") as fp:
   #    msg.attach("image.png", "image/png", fp.read())

   mail.send(msg)
   return make_response("Sent", 200)

if __name__ == '__main__':
   app.run(debug = True)

