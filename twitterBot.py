#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver')
driver.get("https://twitter.com/i/flow/login")


#as the page have only one input field so we can location it by parameter  "//input"
#username = driver.find_element_by_xpath("//input")    #xpath is one way to select html tags 
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
username.send_keys("enter username")

#all_buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[@role='button']")))
all_buttons = driver.find_elements_by_xpath("//div[@role='button']")
all_buttons[-2].click()
#time.sleep(5)

#password = driver.find_element_by_XPATH("//input[@type='password']")
#password.send_keys("password")
password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
password.send_keys("enter password")




all_buttons = driver.find_elements_by_xpath("//div[@role='button']")
all_buttons[-1].click()

time.sleep(2)
keyword = 'pakistan'
driver.get("https://twitter.com/search?q=" + keyword +"&src=typed_query&f=top")

print("**********************************************************************")


time.sleep(5)
likes = driver.find_elements_by_xpath("//div[contains(@aria-label, ' Like')]")
print(likes)

#likes[0].click() 


for likeIcon in likes:
    print("sleeping before liking")
    time.sleep(4)
    likeIcon.click()
    time.sleep(4)
    likeIcon.click()

while 1:
    pass
