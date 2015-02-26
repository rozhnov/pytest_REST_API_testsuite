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
        page.openpage()

        conf = {
                'driver: ': str(driver.capabilities),
                'hub': str(hub),
                'page': page.__class__.__name__
        }


def setup_function(function):
        driver.refresh()


def test_multiselect():
        page.click_first_multi()
        assert True == page.multi_popup.is_displayed()


def test_multiselect_input_default_text():
        text = page.multi_input_0.text
        assert text , 'Выберите из списка'


def test_multiselect2_delete_element():
        page.click_second_multi()
        page.multi_popup2delete.click()
        text = page.multi_popup2area.text
        assert text is ''


def test_multiselect_window_resize():
        helper.set_window_size_divide_by_2(driver)
        assert True == page.multi_open.is_displayed()


def test_multiselect3_multiple_select():
        page.click_third_multi()
        assert True == page.multiple_popup.is_displayed()
        #добавляем первый оффер
        page.multiple_input.click()
        assert True == page.multiple_options.is_displayed()
        items = page.multiple_items
        offer1 = items[0].text
        items[0].click()
        assert False == page.multiple_options.is_displayed()
        assert True == (offer1 in page.multiple_area.text)
        #добавляем второй оффер
        page.multiple_input.click()
        assert True == page.multiple_options.is_displayed()
        assert True == page.multiple_options.is_displayed()
        items = page.multiple_items
        offer2 = items[0].text
        items[0].click()
        assert False == page.multiple_options.is_displayed()
        #проверяем наличие обоих выбранных офферов в мультиселекте
        assert True == (offer2 in page.multiple_area.text), "выбранный оффер отсутствует в мультиселекте: %r" % offer2
        assert True == (offer1 in page.multiple_area.text), "выбранный оффер отсутствует в мультиселекте: %r" % offer1


def teardown_function(function):
        helper.screenshot(function, driver)


def teardown_module():
        driver.quit()
