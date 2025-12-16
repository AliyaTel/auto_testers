from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    sleep(3)


def test_find_by_name(driver):
    driver.get('https://www.google.com/?hl=ky')
    text_area = driver.find_element(By.NAME, 'q')
    text_input = 'cat'
    text_area.send_keys(text_input)
    text_area.send_keys(Keys.ENTER)
    assert driver.title == text_input


def test_find_by_id(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.ID, 'id_text_string')
    text_test = 'test'
    text_input.send_keys(text_test)
    text_input.send_keys(Keys.ENTER)
    text_result = driver.find_element(By.CLASS_NAME, 'result-text')
    assert text_result.text == text_test


def test_by_tagname(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'


def test_by_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    link_text = driver.find_element(By.LINK_TEXT, 'Contact')
    assert link_text.text == 'Contact'


def test_by_partial_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    link_text = driver.find_element(By.LINK_TEXT, 'Contact')
    assert link_text.text == 'Contact'


def test_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.CSS_SELECTOR, '#id_email')
    text_input.send_keys('lalala')


def test_xpath(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    text_input.send_keys('lalala')




# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# driver.close()
# driver.quit()


