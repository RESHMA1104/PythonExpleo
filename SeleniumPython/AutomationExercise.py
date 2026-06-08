import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://automationexercise.com"
driver.get(URL)
time.sleep(5)
driver.find_element(By.XPATH, value='//a[@href="/login"]').click()
ele = driver.find_element(By.XPATH, value='//h2[normalize-space()="New User Signup!"]')
if ele.is_displayed():
    print("New User is Displayed")
else:
    print("New User is not Displayed")
driver.find_element(By.NAME, value="name").send_keys("RajuRajuSS")
driver.find_element(By.XPATH, value='//input[@data-qa="signup-email"]').send_keys("RajuRajuS123@gmail.com")
driver.find_element(By.XPATH, value='//button[normalize-space()="Signup"]').click()
driver.find_element(By.ID, value="password").send_keys("RajuS@123")
driver.find_element(By.ID, value="first_name").send_keys("Raju")
driver.find_element(By.ID, value="last_name").send_keys("RajuS")
driver.find_element(By.ID, value="address1").send_keys("Salem")
country = driver.find_element(By.ID, value="country")
select = Select(country)
select.select_by_visible_text("Canada")
driver.find_element(By.ID, value="state").send_keys("Ontario")
driver.find_element(By.ID, value="city").send_keys("Toronto")
driver.find_element(By.ID, value="zipcode").send_keys("666111")
driver.find_element(By.ID, value="mobile_number").send_keys("9807654321")
driver.find_element(By.XPATH, value='//button[normalize-space()="Create Account"]').click()