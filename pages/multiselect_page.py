__author__ = 's.lugovskiy'
from pages.multiselect_locators import MultiselectLocators
from setup import config
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class MultiselectPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.multiselectpage

    def openmainpage(self):
        self.driver.get(self.baseurl)

    @property
    def multi_popup(self):
        """

        :rtype: WebElement
        """
        name = self.driver.find_element(*MultiselectLocators.MULTI_POPUP)
        return name

    def click_first_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"]:eq(0)\').click()')



