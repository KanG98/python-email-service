from flask_mail import Mail, Message

class Mailing(Mail):

  def __init__(self, app, email, password) -> None:
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['TESTING'] = True
    super().__init__(app)
  
