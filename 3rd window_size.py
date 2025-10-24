from selenium import webdriver
import time

viewports=[(1024,768),(378,700),(900,300)]
driver = webdriver.Chrome()
driver.get("https://google.com")

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(3)

finally:
    driver.close()
