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

#driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver')
#url ='http://www.instagram.com'

#driver.get("https://www.facebook.com")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)



#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/home/abdullah/Downloads/chromedriver_linux64/chromedriver', chrome_options=chrome_options)

#open the webpage
driver.get("http://www.facebook.com")

#target username and password fields
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.send_keys("enter email")    #email = xyz@yahoo.com 
password.clear()
password.send_keys("enter password")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!
images = []



for i in [ 'photos_of' , 'photos_all']:
    driver.get("Link to the photos section" + i + "/")  #https://www.facebook.com/xyz/photos_of
    time.sleep(5)
'''

    n_scrolls = 2
    for j in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


        anchors = driver.find_element(By.TAG_NAME, 'a')
        anchors = driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        
        #print(anchors)    
    #narrow down all links to image links only
        anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
        print(anchors)

    #extract the [1]st image element in each link
        for a in anchors:
            driver.get(a) #navigate to link
            time.sleep(5) #wait a bit
            img = driver.find_elements_by_tag_name("img")
            images.append(img[1].get_attribute("src")) #may change in future to img[?]



path = os.getcwd()
path = os.path.join(path, "FB_SCRAPED")

#create the directory
os.mkdir(path)
print(path)

counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

'''

while 1:
    pass
