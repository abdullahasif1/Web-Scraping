from selenium import webdriver
import time

driver = webdriver.Chrome("/home/abdullah/Downloads/chromedriver_linux64/chromedriver")
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('enter username/email')
password.send_keys('password')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()





#incomplete
