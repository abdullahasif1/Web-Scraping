#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import os
import wget


#s = Service('home/abdullah/Downloads/chromedriver_linux64/chromedriver.exe')

driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver')
#url ='http://www.instagram.com'

driver.get("https://www.facebook.com")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)



#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver', chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("asifabdullah63@yahoo.com")
password.clear()
password.send_keys("806armin")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
while 1:
    pass

