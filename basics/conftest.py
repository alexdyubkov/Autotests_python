import pytest
from selenium import webdriver

@pytest.fixture(scope="function")#фикстура на одну ф-цию
def browser():#фикстура открыть-закрыть браузер хром
    print("\nstart browser fro test...")
    browser=webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()