__author__ = 's.lugovskiy'
from pages.locators import MainPageLocators



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class FrontPage(BasePage):
    def login(self):

        loginlink = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        loginlink.click()
        loginpopup = self.driver.find_element(*MainPageLocators.LOGIN_POPUP)
        name = self.driver.find_element(*MainPageLocators.NICK)
        name.send_keys("me0i@mail.ru")
        pwd = self.driver.find_element(*MainPageLocators.PWD)
        pwd.send_keys("123698745")
        submit = self.driver.find_element(*MainPageLocators.SUBMIT)
        submit.click()
        myname = self.driver.find_element(*MainPageLocators.MYNAME)
        return myname.text


    def getusername(self):
        name = self.driver.find_element(*MainPageLocators.MYNAME)
        return name


