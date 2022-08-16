import os 
from flask_mail import Mail
from server.main import app

def test_mailing():
  app.app_context().push()

  mail= Mail(app)
  email = 'yankang198.dev@gmail.com'

  # need to link mail to mail obj
  with mail.record_messages() as outbox:

      mail.send_message(subject='testing',
                        sender= email, 
                        body='test',
                        recipients=["yankang198@gmail.com"]
                        )

      assert len(outbox) == 1
      assert outbox[0].subject == "testing"