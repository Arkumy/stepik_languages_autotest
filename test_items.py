from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    time.sleep(5)
    button = len(browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button'))
    assert button > 0, 'Element basket not found'

