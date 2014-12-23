import json
import os
import pprint
from jsonschema import validate
from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    pp = pprint.PrettyPrinter()
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/offer-links/4325?")
    jsondump = request.json()
    code = request.status_code


def test_offerlinks_json_status():
    assert code == 200


def test_offerlinks_total_json():
    assert jsondump['data']['total'] > 0
    assert jsondump['error'] == ''


def test_offerlinks_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json not 500"


def test_offerlinks_promo_code():
    items = jsondump['data']['items']
    for item in items:
        assert len(item['title']) > 0
        assert type(item['is_default']) is bool
        assert len(item['deep_link']) > 0


def teardown_module():
    print('teardown module ' + __name__)
    print('\n----------------------------------------------------------------------\n')













