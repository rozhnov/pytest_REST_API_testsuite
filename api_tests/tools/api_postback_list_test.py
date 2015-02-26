import json
import os
import pprint
import random
from jsonschema import validate
from sender.request_sender import Sender
from collections import OrderedDict
import time


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global sender
    global postback_name
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)

    # random data for postback
    postback_name = str(random.randint(1000, 9000))

    # POST parameters with random name
    params = {"query_params": ''}

    # send request
    sender = Sender()
    request = sender.post("/api/rest/webmaster/json/postback?", params)
    jsondump = request.json()

    # print response
    pp = pprint.PrettyPrinter()
    print('response: ')
    pp.pprint(jsondump)
    code = request.status_code
    curdir = os.path.dirname(__file__)


def test_postback_list_json_status():
    assert code == 200


def test_postback_list_json_status_400_or_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"
    assert status != 400, "assert status in json  not 400"


def test_postback_list():
    postback_id = jsondump['data']['id']
    time.sleep(15)
    assert id is not None
    assert id is not ''
    postback = sender.get("/api/rest/webmaster/json/postback-list/?limit=999999&").json()
    assert any(str(postback_id) in item['id'] for item in postback['data']) is True
















