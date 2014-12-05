# -*- coding: utf-8 -*-
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from sender.request_sender import Sender
from setup import helper
from setup import config
from pages import multiselect_page


def setup_module():
        global driver
        global hub
        global page
        global sender
        global conf
        sender = Sender()
        hub = config.hub
        driver = webdriver.Remote(
                command_executor=hub,
                desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.maximize_window()
        page = multiselect_page.MultiselectPage(driver)
        page.openmainpage()

        conf = {
                'driver: ': str(driver.capabilities),
                'hub': str(hub),
                'page': page.__class__.__name__
        }


def setup_function(function):
        driver.refresh()


def test_multiselect():
        page.click_first_multi()
        test_id = '260'

        try:
                assert True == page.multi_popup.is_displayed()
                sender.post_testrail(test_id, 1, conf)
        except AssertionError as e:
                sender.post_testrail(test_id, 5, e)
                raise AssertionError(e)


def test_multiselect_input_default_text():
        test_id = '248'
        text = page.multi_input.text
        try:
                assert text , 'Выберите из списка'
                conf['comment'] = 'Text in input: ' + text
                sender.post_testrail(test_id, 1, conf)
        except AssertionError as e:
                sender.post_testrail(test_id, 5, e)
                raise AssertionError(e)


def test_multiselect2_delete_element():
        test_id = '256'
        try:
                page.click_second_multi()
                page.multi_popup2delete.click()
                text = page.multi_popup2area.text
                assert text is ''
                conf['comment'] = 'multiselect area text: ' + text
                sender.post_testrail(test_id, 1, conf)
        except Exception as e:
                sender.post_testrail(test_id, 5, e)
                raise Exception(e)


def test_multiselect_window_resize():
        test_id = '243'
        try:
                size = helper.set_window_size_divide_by_2(driver)
                assert True == page.multi_open.is_displayed()
                conf['comment'] = 'New window size: ' + str(size)
                sender.post_testrail(test_id, 1, conf)
        except Exception as e:
                sender.post_testrail(test_id, 5, e)


def teardown_function(function):
        helper.screenshot(function, driver)


def teardown_module():
        driver.quit()
