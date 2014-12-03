from setup import helper
from setup import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from pages import multiselect_page


def setup_module():
        global driver
        global hub
        global page
        hub = config.hub
        driver = webdriver.Remote(
            command_executor=hub,
            desired_capabilities=DesiredCapabilities.FIREFOX)
        page = multiselect_page.MultiselectPage(driver)
        page.openmainpage()


def test_multiselect():
        page.click_first_multi()
        assert True == page.multi_popup.is_displayed()


def teardown_function(function):
        helper.screenshot(function, driver)


def teardown_module():
        driver.quit()
