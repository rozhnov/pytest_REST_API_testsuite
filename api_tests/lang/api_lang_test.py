import json
import os
import pprint
import random
from jsonschema import validate
from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global sender
    global rotator_name
    global lang_set
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)

    # PUT parameters
    lang_set = 'en'
    params = {"lang": lang_set}
    # send request for lang change to EN
    sender = Sender()
    request = sender.put("/api/rest/webmaster/json/user-language/?", params)
    jsondump = request.json()

    #print response
    pp = pprint.PrettyPrinter()
    print('response: ')
    pp.pprint(jsondump)
    code = request.status_code


def test_lang_json():
    assert code, 200
    status = jsondump['status']
    assert status is not 500, 400
    profile = sender.get("/api/rest/webmaster/json/profile?").json()
    lang = profile['data']['language']
    assert lang == lang_set


def test_lang_json_status_400_or_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"
    assert status != 400 , "assert status in json  not 400"


def teardown_module():
    print('teardown module ' + __name__)
    print('\n----------------------------------------------------------------------\n')













