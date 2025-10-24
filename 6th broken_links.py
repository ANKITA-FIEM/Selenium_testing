import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://jqueryui.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

links = driver.find_elements(By.TAG_NAME, "a")
print("Total no of links:", len(links))

for link in links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print("Broken link:", href, "Status code:", response.status_code)
    #else:
        #print("OK link:", href, "Status code:", response.status_code)
driver.quit()
