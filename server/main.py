import os 
import platform
from flask import Flask, request, make_response
from mailing import Mailing, Message
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
   return make_response("hello world", 200)

@app.route("/mailing", methods = ["POST"])
def mailing():
   try:
      form = dict(request.form.lists())
      email = form['email'][0]
      password = form['password'][0]
      subject = form['subject'][0]
      recipients = form['recipients']
      html = form['html'][0]
      mail= Mailing(app, email, password)
      mail.send_html(subject, email, recipients, html)
   except Exception as err:
      errorKey = err.__class__.__name__
      return make_response(errorKey, 500)
   return make_response(form, 200)

if __name__ == '__main__':
   app.run(debug = True)

