import time
import sys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from pages import frontpage


def setup_module():
    global driver
    global user
    driver = webdriver.Remote(
        command_executor='http://10.8.15.52:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)
    user = 'me0i@mail.ru'


def teardown_module():
    date = time.strftime("%Y-%m-%d-%H-%M")
    driver.get_screenshot_as_file('screenshots/' + testname + ' ' + str(date) + '.png')
    driver.quit()


def test_login():
    global testname
    testname = sys._getframe().f_code.co_name
    page = frontpage.FrontPage(driver)
    driver.get('http://cityads.com')
    myname = page.login()
    assert (myname == user)












