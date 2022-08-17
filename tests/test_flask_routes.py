import pytest
import json
from server.main import app

@pytest.fixture
def mailing_form():
  mail = {"email": "me", "password": "password", "recipients": ["you"], "html": "<b>hi<b>"}
  return mail

def test_index():
  with app.test_client() as client:
    response = client.get("/")
    assert response.status_code == 200 
    assert response.data == b"hello world"

def test_mail_route(mailing_form):
  with app.test_client() as client:
    response = client.post("/mailing", data=mailing_form, content_type="application/x-www-form-urlencoded")
    print(json.loads(response.data.decode()))
    print(mailing_form)
    assert response.status_code == 200 
    assert json.loads(response.data.decode()).keys() == mailing_form.keys()