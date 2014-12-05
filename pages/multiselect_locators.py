__author__ = 's.lugovskiy'
from selenium.webdriver.common.by import By


class MultiselectLocators(object):
    # multi 1
    MULTI_POPUP = (By.XPATH, '//div[@id="multiselect-0"]/div[@class="multiselect-popup"]')
    MULTI_INPUT = (By.XPATH, '//div[@id="multiselect-0"]/span[@class="multiselect-selected"]')
    MULTI_OPEN = (By.XPATH, '(//td/div[@class="multiselect  closed"]/div[@class="multiselect-button"])[1]')

    # multi 2
    MULTI_POPUP2 = (By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]')
    MULTI_POPUP2_DELETE = (By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]/div[@class="multiselect-area"]/div/span[contains(@class,"multiselect-delete")]')
    MULTI_POPUP2_AREA = (By.XPATH, '//div[@id="multiselect-1"]/div[@class="multiselect-popup"]/div[@class="multiselect-area"]')
