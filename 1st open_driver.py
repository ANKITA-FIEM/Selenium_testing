from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://selenium.dev/")
browser.maximize_window()

time.sleep(3)
title= browser.title
print(title)

assert "Selenium" in title
