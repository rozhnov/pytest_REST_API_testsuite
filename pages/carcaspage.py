from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
from setup import config
from selenium.webdriver.remote.webelement import WebElement


class CarcasPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.baseUrl

    @property
    def __statisticlink(self):
        return self.driver.find_element(By.XPATH, "//a[@id='menuId339']")

    def go_to_old_statistic(self):
        self.__statisticlink.click()

