import time
import sys
from setup import helper
from setup import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from pages import frontpage, carcaspage, oldtablepage
# -*- coding: utf-8 -*-


def setup_module():
    global driver
    global user
    global hub
    global front
    global carcas
    global table
    hub = config.hub
    driver = webdriver.Remote(
        command_executor=hub,
        desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(10)
    driver.maximize_window()
    user = config.wm
    #create page objects
    front = frontpage.FrontPage(driver)
    carcas = carcaspage.CarcasPage(driver)
    table = oldtablepage.OldTablePage(driver)


def teardown_function(function):
    helper.screenshot(function, driver)


def teardown_module():
    driver.quit()


def test_login():
    front.openmainpage()
    front.login()
    front.switch_old_interface()
    carcas.go_to_old_statistic()
    table.click_update()
    lines = table.tabletr
    assert len(lines) > 4
    for line in lines:
        assert line.text is not ''
        assert line.text is not None
















