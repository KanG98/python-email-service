import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_mailing_form():

  service = Service(executable_path=ChromeDriverManager().install())
  opts = Options()
  opts.add_argument('--headless')
  opts.add_argument('--no-sandbox')
  opts.add_argument('--disable-dev-shm-usage')
  opts.add_argument("--remote-debugging-port=8473")
  browser = webdriver.Chrome(service=service, options=opts)
  browser.get('http://google.com/')

  assert "No results found." not in browser.page_source
  browser.close()
