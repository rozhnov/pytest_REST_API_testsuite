__author__ = 's.lugovskiy'
from selenium.webdriver.common.by import By


class MultiselectLocators(object):
    MULTI_POPUP = (By.XPATH, '//div[@id="multiselect-0"]/div[@class="multiselect-popup"]')
