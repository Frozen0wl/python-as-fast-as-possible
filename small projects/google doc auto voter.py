import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
link = "https://docs.google.com/forms/d/e/1FAIpQLSfgAs743bA55YvxNa57XYQnqiTN8EpYf2jgRVVV4AclXACnpg/viewform"
driver.get(link)
fxp = '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/input'
weiter = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span'

senden = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span/span'
zeit = time.time()
counter = 0
while time.time()-zeit<3600:
    print(counter, time.time()-zeit)
    counter += 1
    person = 3
    melih = f'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[{str(person)}]/label/div/div[2]/div/span'
    time.sleep(0.3)

    d=driver.find_element_by_xpath(fxp)
    d.send_keys(counter)

    w = driver.find_element_by_xpath(weiter)
    w.click()

    m=driver.find_element_by_xpath(melih)
    m.click()

    s = driver.find_element_by_xpath(senden)
    s.click()
    driver.get(link)


