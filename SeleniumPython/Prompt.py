import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
URL ="https://www.leafground.com/"
driver.get(URL)
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@href="#"]//child::i[@class="pi pi-globe layout-menuitem-icon"]'))).click()
wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Alert'))).click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@class="card"]//child::button[@id="j_idt88:j_idt104"]'))).click()
alert = driver.switch_to.alert
alert.send_keys("Reshma")
alert.accept()
print("Prompt alert")