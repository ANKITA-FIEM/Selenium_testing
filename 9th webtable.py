from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)
