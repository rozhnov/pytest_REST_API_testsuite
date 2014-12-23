import json
import os
import pprint
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
    request = sender.get("/api/rest/webmaster/json/offertarget/4325?")
    jsondump = request.json()
    code = request.status_code


def test_offerretarget_json_status():
    assert code == 200


def test_offerretarget_total_json():
    assert jsondump['error'] == ''


def test_offerretarget_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json not 500"


def test_offerretarget_promo_code():
    service_area = jsondump['data']['items'][0]['service_area']
    assert len(service_area) > 0
    for item in service_area:
        assert type(item['title']) is str
        assert len(item['title']) > 0
