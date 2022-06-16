#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget


driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver')

driver.get("https://www.instagram.com/")



#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password(first clear then enter
username.clear()
username.send_keys("abdullaahasif")
password.clear()
password.send_keys("806arminn")


#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

import time

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

#search for the hashtag cat
keyword = "#cats"
searchbox.send_keys(keyword)
 
# Wait for 5 seconds
#time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
#searchbox.send_keys(Keys.ENTER)
time.sleep(5)

#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))


path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

os.mkdir(path)

#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1


while 1:
    pass
