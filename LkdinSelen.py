from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome("/home/abdullah/Downloads/chromedriver_linux64/chromedriver")

driver.get("https://linkedin.com")
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")


username.send_keys("enter email")
password.send_keys("password")
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)


while 1:
    pass                  #incomplete
