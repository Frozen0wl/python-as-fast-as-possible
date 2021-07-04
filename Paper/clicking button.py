# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
# driver = webdriver.Chrome(path)


# driver.get("https://techwithtim.net")
# print(driver.title)

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# print(driver.page_source)

# driver.quit()

################################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
# driver = webdriver.Chrome(path)

# driver.get("https://techwithtim.net/")

# link = driver.find_element_by_link_text("Python Programming")
# link.click()

###################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://euw.op.gg/summoner/userName=critzzzzzzz")
time.sleep(15)
link = driver.find_element_by_id("SummonerRefreshButton")
print(link)
