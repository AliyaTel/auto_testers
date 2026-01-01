from playwright.sync_api import Page, expect
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_1(page:Page):
    page.goto('https://www.qa-practice.com/')
    page.get_by_text('Single checkbox').click()
    page.locator('[name="checkbox"]').check()
    page.locator('[name="submit"]').click()
    expect(page.locator('[id="result-text"]')).to_contain_text('select me or not')
    page.screenshot(path="page.png")
    page.keyboard.press("Enter")
    sleep(5)


def test_2(page:Page):
    page.goto('https://demoqa.com/text-box')
    page.locator('[id="userName"]').fill("Hello!")
    sleep(5)


def test_3(page:Page):
    page.goto('https://demoqa.com/text-box')
    page.locator('[id="userEmail"]').fill("jjjjj888@gmail.com")
    sleep(5)


def test_4(page:Page):
    page.goto('https://demoqa.com/text-box')
    page.locator('[id="currentAddress"]').fill("bishkekcity")
    sleep(10)


# def test_for_alfia():
#     driver = webdriver.Chrome()
#     driver.get("https://www.qa-practice.com/contact/")
#     message = driver.find_element(By.ID, "id_message")
#     message.send_keys("Hello QA")
#     time.sleep(5)
#     wait = WebDriverWait(driver, 10)
#     submit = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/input[2]")))
#     driver.execute_script("arguments[0].click();", submit)
#     time.sleep(10)
#     driver.quit()
# # test_for_alfia()


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "test",
        "body": "hello",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "userId" in data
    assert data["userId"] == 1
    assert data["title"] == "test"


def test_get_all_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_one_product():
    url = "https://fakestoreapi.com/products/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1


def test_checkboxes():
    driver = webdriver.Chrome()
    driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    checkboxes = driver.find_elements(By.NAME, "checkboxes")
    checkboxes[0].click()
    submit = driver.find_element(By.NAME, "submit")
    submit.click()
    sleep(10)
    driver.close()


def test_add_new_user():
    url = "https://fakestoreapi.com/users"
    payload = {
        "id": 1,
        "username": "ghf_fkfj",
        "email": "qa@test.com",
        "password": "1575846"
    }
    response = requests.post(url, json=payload)
    assert response.status_code in [201]
    data = response.json()
    print(data)
    assert "id" in data






