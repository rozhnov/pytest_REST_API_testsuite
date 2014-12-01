import time
import sys

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from nose import with_setup

from pages import frontpage


class Logintest:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://10.8.15.52:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.user = 'me0i@mail.ru'

    def teardown(self):
        date = time.strftime("%Y-%m-%d-%H-%M")
        self.driver.get_screenshot_as_file('screenshots/' + self.testname + ' ' + str(date) + '.png')
        self.driver.quit()

    @with_setup('', teardown)
    def wm_login_test(self):
        self.testname = sys._getframe().f_code.co_name
        page = frontpage.FrontPage(self.driver)
        self.driver.get('http://cityads.com')
        myname = page.login()
        assert (myname == self.user)












