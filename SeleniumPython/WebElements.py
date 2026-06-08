import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

URL = "https://www.google.co.in"
driver.get(URL)

print(driver.title)
time.sleep(2)

ele = driver.find_element(By.NAME, value='q')

# Check enabled
if ele.is_enabled():
    print("Element is Enabled")
else:
    print("Element is not enabled")
ele.send_keys("Selenium")
ele.send_keys(Keys.ENTER)

time.sleep(3)

ele1 = driver.find_element(By.NAME, value='btnK')

# Check enabled
if ele1.is_enabled():
    print("Element1 is enabled")
else:
    print("Element1 is not enabled")
ele1.click()

time.sleep(5)
driver.close()