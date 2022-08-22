import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_mailing_form():
  
  # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver = webdriver.Firefox()
  driver.get("file:///"+os.getcwd()+"/client/index.html")
  elem = driver.find_element(By.ID, "email")
  elem.send_keys("hi")
  elem.send_keys(Keys.RETURN)
  assert "No results found." not in driver.page_source
  driver.close()