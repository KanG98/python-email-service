import email
import os
import platform
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
  system = platform.system()
  service = Service()
  if (system == "Darwin"):
    service = Service(executable_path='/opt/homebrew/bin/chromedriver')
  elif (system == "Linux"):
    service = Service(executable_path='/usr/bin/chromedriver')
  opts = Options()
  opts.add_argument('--headless')
  opts.add_argument('--no-sandbox')
  opts.add_argument('--disable-dev-shm-usage')
  # opts.add_argument("--remote-debugging-port=4748")
  browser = webdriver.Chrome(service=service, options=opts)
  return browser
  

def test_mailing_form_fail(browser):
  browser.get('file:///'+os.getcwd()+'/client/index.html')
  print(browser.page_source)

  # browser.get_screenshot_as_file("./screenshot.png")

  email_input = browser.find_element(By.ID, "email")
  email_input.send_keys("testEmail")
  email_input.send_keys(Keys.RETURN)


  print(browser.page_source)
  assert "KeyError" in browser.page_source
  
  browser.close()
