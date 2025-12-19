import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    sleep(100)

def test_find_by_name(driver):
    driver.get("https://www.google.com/?hl=ru")
    text_area = driver.find_element(By.NAME, "q")
    text_input = "cat"
    text_area.send_keys(text_input)
    text_area.send_keys(Keys.ENTER)
    assert driver.title == text_input


def test_find_by_id(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_input = driver.find_element(By.ID,"id_text_string")
    text_test = "test"
    text_input.send_keys(text_test)
    text_input.send_keys(Keys.ENTER)
    text_result = driver.find_element(By.CLASS_NAME,"result-text")
    assert text_result.text == text_test


def test_first_multiselect(driver):
    driver.get('https://www.qa-practice.com/elements/select/mult_select')
    select = driver.find_element(By.NAME, "choose_the_place_you_want_to_go")
    location_select = Select(select)
    location_select.select_by_value("4")
    assert location_select.first_selected_option.is_selected()


def test_find_by_css_selector(driver):
    driver.get("https://www.qa-practice.com/elements/select/mult_select")
    select_element = driver.find_element(By.CSS_SELECTOR, "select[name ='choose_how_you_want_to_get_there']")
    transport_select = Select(select_element)
    transport_select.select_by_value("2")
    assert transport_select.first_selected_option.is_selected()



