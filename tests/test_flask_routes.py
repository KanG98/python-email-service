import pytest
import json
import os
from server.main import app

@pytest.fixture
def complete_mailing_form():
  mail = {
          "email": "yankang198.dev@gmail.com", 
          "password": os.getenv('EMAIL_PASSWORD'), 
          "subject": "hi", 
          "recipients": ['yankang198@gmail.com'], 
          "html": "<b>hi<b>"
          }
  return mail

@pytest.fixture
def incomplete_mailing_form():
  mail = {
          "email": "yankang198.dev@gmail.com", 
          "subject": "hi", 
          "recipients": ['yankang198@gmail.com'], 
          "html": "<b>hi<b>"
          }
  return mail

def test_index():
  with app.test_client() as client:
    response = client.get("/")
    assert response.status_code == 200 
    assert response.data == b"hello world"

def test_mail_route_success(complete_mailing_form):
  with app.test_client() as client:
    response = client.post("/mailing", data=complete_mailing_form, content_type="application/x-www-form-urlencoded")
    assert response.status_code == 200 
    assert json.loads(response.data.decode()).keys() == complete_mailing_form.keys()

def test_mail_route_fail(incomplete_mailing_form):
  with app.test_client() as client:
    response = client.post("/mailing", data=incomplete_mailing_form, content_type="application/x-www-form-urlencoded")
    assert response.data == b'KeyError'