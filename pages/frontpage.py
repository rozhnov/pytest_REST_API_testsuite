__author__ = 's.lugovskiy'
from pages.locators import MainPageLocators
from setup import config
from selenium.webdriver.remote.webelement import WebElement


class FrontPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.baseUrl

    def login(self):
        self.loginlink.click()
        self.name.send_keys("me0i@mail.ru")
        self.pwd.send_keys("123698745")
        self.submit.click()
        return self.myname.text

    def openmainpage(self):
        self.driver.get(self.baseurl)

    @property
    def username(self):
        """

        :rtype: WebElement
        """
        name = self.driver.find_element(*MainPageLocators.MYNAME)
        return name

    @property
    def loginlink(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.LOGIN_LINK)

    @property
    def loginpopup(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.LOGIN_POPUP)

    @property
    def name(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.NICK)

    @property
    def pwd(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.PWD)

    @property
    def submit(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.SUBMIT)

    @property
    def myname(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(*MainPageLocators.MYNAME)
