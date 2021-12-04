from pages.product_page   import ProductPage
#import time#временно



def test_product_page_open_and_click_putinthebasket(browser):
    #link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"  #link to test1
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"         #link to test2
    page = ProductPage(browser,link)
    page.open()
    page.product_page_click_putinthebasket()
    page.solve_quiz_and_get_code()
    page.what_was_added_to_a_bucket()
