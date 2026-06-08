from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://automationexercise.com"
driver.get(URL)
wait = WebDriverWait(driver, 5)
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
try:
    driver.find_element(By.XPATH, '//div[@aria-label="Close ad"]').click()
except:
    pass
driver.switch_to.default_content()
actual_text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[text()= " Home"]'))).text
assert 'Home' in actual_text, "Home is not visible"
print("Home is visible")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(),  'Test Cases')]"))).click()
testcase_text = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//h2[@class="title text-center"]//child::b'))).text
assert 'TEST CASES' in testcase_text.upper(), "Test case page is not visible"
print("Test cases is visible")
driver.close()