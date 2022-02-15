from selenium import webdriver

import time

url = "https://der-artikel.de/"

op = webdriver.ChromeOptions() # makes the browser invisible
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get(url)

input = driver.find_element_by_id('word')
# button.click()
input.send_keys('abstand')

searchButton = driver.find_element_by_class_name('icon-magnifier')
searchButton.click() 

time.sleep(0.1)

element = driver.find_element_by_class_name("mb-1").text
driver.close()
driver.quit()
print(element)

