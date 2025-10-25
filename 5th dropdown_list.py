import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window()

url = "https://the-internet.herokuapp.com/dropdown"
driver.get(url)

dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
select.select_by_visible_text("Option 2")
option_count = len(select.options)
time.sleep(1)
expected_count = 3
if option_count == expected_count:
    print("test passed for option count")
else:
    print("test failed for option count")
time.sleep(3)

target_value = "Option 3"

for option in select.options:
    if option.text == target_value:
        option.click()
        print("option selected is:", target_value)
        break
    else:
        print("option is not selected")

time.sleep(3)
driver.quit()



