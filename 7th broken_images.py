import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME,"img")
broken_images = []

for image in images:
    scr = image.get_attribute("src")
    if scr:
        response = requests.get(scr)
        if response.status_code != 200:
            broken_images.append(scr)
            print("Broken images:", scr, "Status code:", response.status_code)

if broken_images:
    print("List of broken images:", broken_images)
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images")

driver.quit()


