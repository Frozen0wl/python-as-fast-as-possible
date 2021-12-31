from selenium import webdriver

def getArticle(word:str):
    url = "https://www.verbformen.com/declension/nouns/?w="+word

    op = webdriver.ChromeOptions() # makes the browser invisible
    op.add_argument('headless')
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=op)

    driver.get(url)

    
    # element = driver.find_element_by_xpath("/html/body/article/div[1]/div[3]/div/section[1]/p[2]/text()").text does not work for some reason
    element = driver.find_element_by_xpath("/html/body/article/div[1]/div[3]/div/section[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]").text
    return(element)

