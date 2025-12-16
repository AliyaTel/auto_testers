from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    # browser.implicitly_wait(5)
    yield browser
    sleep(3)


def test_clear(driver):
    driver.get('https://www.google.com/?hl=ky')
    text_area = driver.find_element(By.NAME, 'q')
    text_area.send_keys('lalalalal')
    print(text_area.text)
    text_area.clear()
    text_area.send_keys('dadadadadad')
    print(text_area.text)


def test_enabled_and_selected(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, 'submit')
    print(button.is_enabled())
    select = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())
    button.is_displayed()


def test_wait(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()


def test_wait_wait(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button3 = driver.find_element(By.ID, 'visibleAfter')
    driver.execute_script("arguments[0].scrollIntoView(true);", button3)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button3.click()



