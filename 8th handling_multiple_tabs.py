import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()

driver.switch_to.new_window()
driver.get("https://playwright.dev/")
time.sleep(1)

number_of_tabs = len(driver.window_handles)
print("Number of tabs:", number_of_tabs)

tabs_value = driver.window_handles
print("TAB VALUES:", tabs_value)

current_tab = driver.current_window_handle
print("Current tab:", current_tab)

driver.find_element(By.CSS_SELECTOR, "#__docusaurus_skipToContent_fallback > header > div > div > a").click()
time.sleep(3)
FirstTab = driver.window_handles[0]
if current_tab != FirstTab:
    driver.switch_to.window(FirstTab)
driver.find_element(By.XPATH,"/html/body/header/nav/div/ul/li[2]/a/span").click()
time.sleep(2)

driver.quit()

