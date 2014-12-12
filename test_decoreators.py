__author__ = 's.lugovskiy'
import os.path
import decorator
import datetime


def log_test(func):
    def step(func, *args, **kwargs):
        now = datetime.datetime.now()
        try:
            func(*args)
            result = 'ok'
            save_test(func, args, result)
        except Exception as e:
            result = str(e)
            save_test(func, args, result)
            raise e
    return decorator.decorator(step, func)


def save_test(func, args, result):
    now = datetime.datetime.now()
    curdir = os.path.dirname(__file__)
    fname = func.__name__
    name = (str(fname + now.strftime("%A-%d.%B-%Y-%I-%M-%p-")))
    path = curdir + "/reports/" + name
    if result is 'ok':
        path += '_PASSED' + '.html'
    else:
        path += '_FAILED' + '.html'

    if os.path.isfile(path):
        with open(path, "a") as file:
            file.write(func.__name__ + str(args) + '<p>' + result + '<p/>' + '<br>')
    else:
        file = open(path, 'w+')
        file.write(func.__name__ + str(args) + '<p>' + result + '<p/>' + '<br>')