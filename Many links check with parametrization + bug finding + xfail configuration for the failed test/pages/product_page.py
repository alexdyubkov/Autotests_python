from conftest import browser
from .base_page import BasePage
from .product_page_locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException 
import pytest

class ProductPage(BasePage): #наследуем BasePage для ProductPage
    def product_page_click_putinthebasket(self): #внутренности открития страницы
        button_putinthebasket = self.browser.find_element(*ProductPageLocators.button_putinthebasket_link) #из locators.py находим элемент для клика
        button_putinthebasket.click()

    def what_was_added_to_a_bucket(self):
        bucket_element = self.browser.find_element(*ProductPageLocators.elementname_in_bucket)
        bucket_element = bucket_element.text

        element_you_clicked = self.browser.find_element(*ProductPageLocators.element_you_clicked)
        element_you_clicked = element_you_clicked.text

        bucket_element_price = self.browser.find_element(*ProductPageLocators.price_in_bucket)
        bucket_element_price = bucket_element_price.text


        assert bucket_element == element_you_clicked, f'element you bought({bucket_element}) and element in you bucket({element_you_clicked}) are different !'
        print('Now in your bucket: ' + bucket_element + ' ' +  str(bucket_element_price))

