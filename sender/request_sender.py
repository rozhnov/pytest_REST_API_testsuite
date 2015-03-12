__author__ = 's.lugovskiy'

import pprint
import requests
from setup import config
from testrail import testrail
import json


class Sender:

    def __init__(self):
        self.url = config.apiurl
        self.rail_api = config.testrail_post_api
        self.key = config.key
        self.token = 'remote_auth=' + self.key
        self.testrail_run_id = config.testrail_runid
        self.pp = pprint.PrettyPrinter()

    def get(self, method):
        fullurl = self.url + method + self.token
        print('\nGET ' + fullurl)
        request = requests.get(self.url + method + self.token, verify=False)
        return request

    def post(self, method, params=None):
        fullurl = self.url + method + self.token
        print('\nPOST ' + fullurl)
        print('\nparams: ' + json.dumps(params))
        request = requests.post(self.url + method + self.token, data=json.dumps(params), verify=False)
        return request

    def post_without_token(self, method, params=None):
        fullurl = self.url + method
        print('\nPOST ' + fullurl)
        print('\nparams: ' + json.dumps(params))
        request = requests.post(self.url + method + self.token, data=json.dumps(params), verify=False)
        return request

    def post_xml(self, method, params=None):
        fullurl = self.url + method + self.token
        print('\nPOST ' + fullurl)
        print('\nparams: ' + params)
        request = requests.post(self.url + method + self.token, data=params, verify=False)
        return request

    def put_xml(self, method, params=None):
        fullurl = self.url + method + self.token
        print('\nPUT ' + fullurl)
        print('\nparams: ' + params)
        request = requests.put(self.url + method + self.token, data=params, verify=False)
        return request

    def put(self, method, params=None):
        fullurl = self.url + method + self.token
        print('\nPUT ' + fullurl)
        print('\nparams: ' + json.dumps(params))
        request = requests.put(self.url + method + self.token, data=json.dumps(params), verify=False)
        return request

    def post_testrail(self, testid, status, comment='ok'):
        client = testrail.APIClient(self.rail_api)
        client.user = 'autotest@team.sagl'
        client.password = '123456'
        url = 'add_result_for_case/' + str(self.testrail_run_id) + '/' + str(testid)
        res = {'status_id': status, 'comment': str(comment)}
        result = client.send_post(url, res)

