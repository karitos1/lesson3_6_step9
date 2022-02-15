from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_presence(browser):
    browser.get(link)
    basket_btn = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(basket_btn) > 0, "Нет кнопки добавления в корзину"
