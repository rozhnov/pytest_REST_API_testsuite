from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
from setup import config
from selenium.webdriver.remote.webelement import WebElement


class FrontPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.baseUrl

    @property
    def __username(self):
        name = self.driver.find_element(By.XPATH, "//a[@class='with-hover-underline col-blacky']")
        return name

    @property
    def __loginlink(self):
        return self.driver.find_element(By.XPATH, '//a[@id="popup-login-link"]')

    @property
    def __loginpopup(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'popup popup-logi')]")

    @property
    def __name(self):
        return self.driver.find_element(By.XPATH, '//input[@name="nick"]')

    @property
    def __pwd(self):
        return self.driver.find_element(By.XPATH, '//input[@name="passwd"]')

    @property
    def __submit(self):
        return self.driver.find_element(By.XPATH, '//span[@class="submit"]')

    @property
    def __myname(self):
        return self.driver.find_element(By.XPATH, "//a[@class='with-hover-underline col-blacky']")

    @property
    def __old(self):
        return self.driver.find_element(By.XPATH, "//a[@id='account_type_switch_to_old']")

    def login(self):
        self.__loginlink.click()
        self.__name.send_keys("me0i@mail.ru")
        self.__pwd.send_keys("123698745")
        self.__submit.click()
        return self.__myname.text

    def openmainpage(self):
        self.driver.get(self.baseurl)

    def switch_old_interface(self):
        self.__old.click()

