from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#checkboxes=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div[1]/label").click()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
time.sleep(8)
checked_count=0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1
expected_checked_count = 10

if checked_count == expected_checked_count:
    print("Checked")
else:
    print("Not Checked")

driver.quit()




