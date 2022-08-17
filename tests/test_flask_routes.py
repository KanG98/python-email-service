import pytest
from server.main import app

def test_request_example():
  with app.test_client() as fake_client:
    response = fake_client.get("/")
    print(response.data)
    assert True