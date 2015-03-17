from setup import helper
from setup import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
# -*- coding: utf-8 -*-


def setup_module():
    global driver
    global user
    global hub
    hub = config.hub
    driver = webdriver.Remote(
        command_executor=hub,
        desired_capabilities=DesiredCapabilities.CHROME)
    user = config.wm
    driver.get("http://192.168.55.55/")


def teardown_function(function):
    helper.screenshot(function, driver)


def teardown_module():
    driver.quit()


def test_laravel_title():
    text = driver.find_element_by_xpath("//div[@class='title']").text
    assert text == 'Laravel 5'


def test_laravel_quote():
    text = driver.find_element_by_xpath("//div[@class='quote']").text
    size = len(text)
    assert size > 0



