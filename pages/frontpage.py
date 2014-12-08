from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
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
        name = self.driver.find_element(By.XPATH, "//a[@class='with-hover-underline col-blacky']")
        return name

    @property
    def loginlink(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, '//a[@id="popup-login-link"]')

    @property
    def loginpopup(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'popup popup-logi')]")

    @property
    def name(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, '//input[@name="nick"]')

    @property
    def pwd(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, '//input[@name="passwd"]')

    @property
    def submit(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, '//span[@class="submit"]')

    @property
    def myname(self):
        """

        :rtype: WebElement
        """
        return self.driver.find_element(By.XPATH, "//a[@class='with-hover-underline col-blacky']")
