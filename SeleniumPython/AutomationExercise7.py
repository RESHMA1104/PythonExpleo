from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://automationexercise.com"
driver.get(URL)
driver.implicitly_wait(5)
actual_text = driver.find_element(By.XPATH, '//a[text()= " Home"]').text
assert 'Home' in actual_text, "Home is not visible"
driver.find_element(By.XPATH, "//a[contains(text(),  'Test Cases')]").click()
testcase_text = driver.find_element(By.XPATH, '//h2[@class="title text-center"]//child::b').text
assert 'TEST CASES' in testcase_text.upper(), "Test case page is not visible"