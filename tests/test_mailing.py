import os 
from server.mailing import Mailing
from server.main import app

def test_mailing():
  app.app_context().push()

  email = 'yankang198.dev@gmail.com'
  password = os.getenv('EMAIL_PASSWORD')
  mail = Mailing(app, email, password)

  with mail.record_messages() as outbox:

      mail.send_message(subject='testing',
                        sender= email, 
                        body='test',
                        recipients=["yankang198@gmail.com"]
                        )

      assert len(outbox) == 1
      assert outbox[0].subject == "testing"