from selenium import webdriver
import math


class BasePage():#класс "базовая страница" - что умеет каждая страница
    def __init__(self,browser,url): #конструктор для создания инстанса класса
        self.browser = browser
        self.url = url
    
    def open(self): #каждая страница может юзать browser из conftest.py и открывать ссылку
        self.browser.get(self.url)


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")