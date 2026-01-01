from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests


@pytest.fixture
def driver():
    wd = webdriver.Chrome()
    wd.maximize_window()
    yield wd
    wd.quit()

def test_1(driver):
    driver.get("https://www.qa-practice.com/contact")
    driver.find_element(By.NAME, "name").send_keys("login")
    driver.find_element(By.NAME, "email").send_keys("1234")
    driver.find_element(By.ID, "submit-id-submit")
    assert driver.title == 'Contact Us | QA Practice'


def test_2():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "@" in data['email']






