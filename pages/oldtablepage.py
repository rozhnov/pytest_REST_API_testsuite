from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
from setup import config
from selenium.webdriver.remote.webelement import WebElement


class OldTablePage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.baseUrl

    @property
    def tabletr(self):
        return self.driver.find_elements(By.XPATH, "//table[contains(@class,'orange_table')]/tbody/tr[contains(@id,'id_el_tr')]")

    @property
    def __update(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_el_link_update']")

    def click_update(self):
        self.__update.click()


