from selenium.webdriver.common.by import By

__author__ = 's.lugovskiy'
from setup import config


class MultiselectPage():
    def __init__(self, driver):
        self.driver = driver
        self.baseurl = config.multiselectpage

    def openpage(self):
        self.driver.get(self.baseurl)

    #ОБЩИЕ
    @property
    def multi_popup_common(self):
        multi_popup = self.driver.find_element(By.XPATH, '//div[@class=\'multiselect open\']/div[@class=\'multiselect-popup\']')
        return multi_popup


    #MUTLI 1
    @property
    def multi_popup(self):
        multi_popup = self.driver.find_element(By.XPATH, '//div[@id="multiselect-0"]/div[@class="multiselect-popup"]')
        return multi_popup

    @property
    def multi_input_0(self):
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

    #MUTLI 2 Множественный выбор
    def click_third_multi(self):
        self.driver.execute_script('$(\'div[class*="multiselect-button"][tabindex="3"]\').click()')

    @property
    def multiple_popup(self):
        multiple_popup = self.driver.find_element(By.XPATH, '//div[@id=\'multiselect-2\']/div[@class=\'multiselect-popup\']')
        return multiple_popup

    @property
    def multiple_input(self):
        multiple_input = self.driver.find_element(By.XPATH, '//div[@id=\'multiselect-2\']/div[@class=\'multiselect-popup\']/div[@class=\'multiselect-list\']/input')
        return multiple_input

    @property
    def multiple_options(self):
        multiple_options = self.driver.find_element(By.XPATH, '//div[@id="multiselect-2"]/div[@class="multiselect-popup"]/div[@class="multiselect-list"]/div[@class="multiselect-options"]')
        return multiple_options

    @property
    def multiple_items(self):
        multiple_items = self.driver.find_elements(By.XPATH, '//div[@id="multiselect-2"]/div[@class="multiselect-popup"]/div[@class="multiselect-list"]/div[@class="multiselect-options"]/span[@class="multiselect-item"]')
        return multiple_items

    @property
    def multiple_area(self):
        multiple_area = self.driver.find_element(By.XPATH, '//div[@id="multiselect-2"]/div[@class="multiselect-popup"]/div[@class="multiselect-area"]')
        return multiple_area