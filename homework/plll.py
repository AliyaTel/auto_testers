from playwright.sync_api import Page, expect
from time import sleep


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








