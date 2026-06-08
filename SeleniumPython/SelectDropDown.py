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
time.sleep(5)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@href="#"]//child::i[@class="pi pi-server layout-menuitem-icon"]'))).click()
wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Dropdown'))).click()
selectdropdown = wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'select')))
select = Select(selectdropdown)
select.select_by_visible_text('Playwright')