__author__ = 's.lugovskiy'
from pages.multiselect_locators import MultiselectLocators
from setup import config


class MultiselectPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.multiselectpage

    def openmainpage(self):
        self.driver.get(self.baseurl)

    #MUTLI 1

    @property
    def multi_popup(self):
        multi_popup = self.driver.find_element(*MultiselectLocators.MULTI_POPUP)
        return multi_popup

    @property
    def multi_input(self):
        multi_input = self.driver.find_element(*MultiselectLocators.MULTI_INPUT)
        return multi_input

    @property
    def multi_open(self):
        multi_open = self.driver.find_element(*MultiselectLocators.MULTI_OPEN)
        return multi_open

    #MUTLI 2
    @property
    def multi_popup2(self):
        multi_popup2 = self.driver.find_element(*MultiselectLocators.MULTI_POPUP2)
        return multi_popup2

    @property
    def multi_popup2delete(self):
        multi_popup2delete = self.driver.find_element(*MultiselectLocators.MULTI_POPUP2_DELETE)
        return multi_popup2delete

    @property
    def multi_popup2area(self):
        multi_popup2area = self.driver.find_element(*MultiselectLocators.MULTI_POPUP2_AREA)
        return multi_popup2area

    def click_first_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"]:eq(0)\').click()')

    def click_second_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"][tabindex="2"]\').click()')

