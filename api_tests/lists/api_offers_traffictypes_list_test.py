import json
import os
from jsonschema import validate
from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/offers-traffictypes-list/web?")
    jsondump = request.json()
    code = request.status_code


def test_api_offers_traffictypes_list_json_status():
    assert code == 200


def test_api_offers_traffictypes_list_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def test_api_offers_traffictypes_list_json():
    data = jsondump['data']
    assert len(data) > 10
    assert len(data) > 0
    for item in data:
        assert len(item['id']) > 0
        assert len(item['name']) > 0

















