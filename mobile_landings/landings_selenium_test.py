import time
import sys
import pprint
import pytest
from setup import helper
from setup import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


def setup_module():
    global driver
    global user
    global pp
    driver = webdriver.Remote(
        command_executor='http://10.8.15.52:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)
    user = config.wm
    driver.maximize_window()
    pp = pprint.PrettyPrinter()


def teardown_function(function):
    helper.screenshot(function, driver)
    driver.delete_all_cookies()
    #driver.get('http://cityads.ru')


def teardown_module():
    driver.quit()


@pytest.mark.parametrize("url", [
    'http://cityredirect.com/click-EQCIDAH0-VRMIQ785?bt=25&tl=1',
    'http://cityredirect.com/click-EQCIDAH0-PNLJQ79F?bt=25&tl=1'
    'http://cityredirect.com/click-EQCIDAH0-RMIQBADF?bt=25&tl=1',
    'http://cityredirect.com/click-EQCIDAH0-HEBQBAEA?bt=25&tl=1',
    'http://cityredirect.com/click-FQCIDAIA-RNKHQ78V?bt=25&tl=1',
    'http://cityredirect.com/click-GQCIDAIK-GECAQ79P?bt=25&tl=1',
    'http://cityredirect.com/click-GQCIDAIK-KHEBQ790?bt=25&tl=1',
    'http://cityredirect.com/click-DQCIDAHP-NKHEQ770?bt=25&tl=1',
    'http://cityredirect.com/click-DQCIDAHP-SNJFQ78A?bt=25&tl=1',
    'http://cityredirect.com/click-DQCIDAHP-NLJQBADP?bt=25&tl=1',
    'http://cityredirect.com/click-DQCIDAHP-HFDQBBTF?bt=25&tl=1',
])
def test_landing(url):
    print('\n-----------------------------------')
    print('test started: ' + url)
    print('get url: ' + url)
    driver.get(url)
    src = driver.page_source
    pp.pprint(src)
    current_url = driver.current_url
    print('current url: ' + current_url)
    assert ('cityredirect' in current_url) is False
    assert ('cityads.com' in current_url) is False
    assert ('cityads.ru' in current_url) is False
    assert ('cityadspix.com' in current_url) is False
    assert ('head' in src) is True











