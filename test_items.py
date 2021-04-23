import pytest
from selenium import webdriver
import time

def test_lang(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_id("add_to_basket_form")
    button.click()
    assert button, 'Такая кнопка не найдена'
    time.sleep(5)


