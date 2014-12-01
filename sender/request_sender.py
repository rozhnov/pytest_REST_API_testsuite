__author__ = 's.lugovskiy'
import requests
from setup import config


class Sender:

    def __init__(self):
        self.url = config.apiurl
        self.key = config.key
        self.token = '&remote_auth=' + self.key

    def get(self, method):
        fullurl = self.url + method + self.token
        print('send GET ' + fullurl)
        request = requests.get(self.url + method + self.token, verify=False)
        return request

