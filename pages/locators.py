__author__ = 's.lugovskiy'
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.XPATH, '//a[@id="popup-login-link"]')
    NICK = (By.XPATH, '//input[@name="nick"]')
    PWD = (By.XPATH, '//input[@name="passwd"]')
    SUBMIT = (By.XPATH, '//span[@class="submit"]')
    MYNAME = (By.XPATH, "//a[@class='with-hover-underline col-blacky']")
    LOGIN_POPUP = (By.XPATH, "//div[contains(@class,'popup popup-logi')]")