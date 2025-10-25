from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(3)
table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(row_count)
target_value = "America"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print("Found Target value:", target_value)
            found = True
            break
    if found:
        break
if not found:
    print("Could not find Target value:", target_value)

driver.quit()

