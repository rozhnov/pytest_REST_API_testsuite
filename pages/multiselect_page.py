from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
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
        multi_popup = self.driver.find_element(By.XPATH, '//div[@id="multiselect-0"]/div[@class="multiselect-popup"]')
        return multi_popup

    @property
    def multi_input(self):
        multi_input = self.driver.find_element(By.XPATH, '//div[@id="multiselect-0"]/span[@class="multiselect-selected"]')
        return multi_input

    @property
    def multi_open(self):
        multi_open = self.driver.find_element(By.XPATH, '(//td/div[@class="multiselect  closed"]/div[@class="multiselect-button"])[1]')
        return multi_open

    #MUTLI 2
    @property
    def multi_popup2(self):
        multi_popup2 = self.driver.find_element(By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]')
        return multi_popup2

    @property
    def multi_popup2delete(self):
        multi_popup2delete = self.driver.find_element(By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]/div[@class="multiselect-area"]/div/span[contains(@class,"multiselect-delete")]')
        return multi_popup2delete

    @property
    def multi_popup2area(self):
        multi_popup2area = self.driver.find_element(By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]/div[@class="multiselect-area"]')
        return multi_popup2area

    def click_first_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"]:eq(0)\').click()')

    def click_second_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"][tabindex="2"]\').click()')

