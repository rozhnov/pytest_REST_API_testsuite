__author__ = 's.lugovskiy'
import time
import os


def screenshot(function, driver):
    path = os.path.dirname(os.path.realpath(__file__)) + '/screenshots/'
    date = time.strftime("%Y-%m-%d-%H-%M")
    filename = path + function.__name__ + '_' + str(date) + '.png'
    png = driver.get_screenshot_as_png()
    f = open(filename, 'wb+')
    f.write(png)
    print('screenshot saved : ')
    print(filename)
