import time
import sys
from setup import helper
from setup import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from pages import frontpage


def setup_module():
    global driver
    global user
    global hub
    hub = config.hub
    driver = webdriver.Remote(
        command_executor=hub,
        desired_capabilities=DesiredCapabilities.FIREFOX)
    user = config.wm


def teardown_function(function):
    helper.screenshot(function, driver)


def teardown_module():
    driver.quit()


def test_login():
    page = frontpage.FrontPage(driver)
    page.openmainpage()
    myname = page.login()
    assert (myname == user)












