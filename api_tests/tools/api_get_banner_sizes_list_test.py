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
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/banner-sizes-list?")
    jsondump = request.json()
    pp = pprint.PrettyPrinter()
    pp.pprint(jsondump)
    code = request.status_code


def test_banners_sizes_list_status():
    assert code == 200


def test_banners_sizes_list_json_status_400_or_500():
    status = jsondump['status']
    assert status != 500
    assert status != 400


def test_banners_sizes_list_data():
    data = jsondump['data']
    assert len(data) > 10
    for item in data:
        assert len(item['id']) > 0
        assert len(item['name']) > 0













