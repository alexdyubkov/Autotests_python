from selenium.webdriver.common.by import By



class ProductPageLocators():
    button_putinthebasket_link = (By.CSS_SELECTOR,"#add_to_basket_form > button") #CSS ссылка на кнопку
    #button_putinthebasket_link=(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")

    elementname_in_bucket = (By.XPATH,"//div[@class='alertinner ']/strong[position()=1]")

    price_in_bucket = (By.XPATH,"//div[@class='alertinner ']/p/strong")
