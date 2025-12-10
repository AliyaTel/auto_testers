import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    sleep(100)

# def test_find_by_name(driver):
#     driver.get("https://www.google.com/?hl=ru")
#     text_area = driver.find_element(By.NAME, "q")
#     text_input = "cat"
#     text_area.send_keys(text_input)
#     text_area.send_keys(Keys.ENTER)
#     assert driver.title == text_input
#
#
# def test_find_by_id(driver):
#     driver.get("https://www.qa-practice.com/elements/input/simple")
#     text_input = driver.find_element(By.ID,"id_text_string")
#     text_test = "test"
#     text_input.send_keys(text_test)
#     text_input.send_keys(Keys.ENTER)
#     text_result = driver.find_element(By.CLASS_NAME,"result-text")
#     assert text_result.text == text_test




def test_email_field(driver):
    driver.get("https://www.qa-practice.com/elements/input/email")

    email_input = driver.find_element(By.ID, "id_text_string")
    valid_email = "user@example.com"

    email_input.send_keys(valid_email)
    email_input.send_keys(Keys.ENTER)

    result = driver.find_element(By.CLASS_NAME, "result-text")
    assert result.text == valid_email




