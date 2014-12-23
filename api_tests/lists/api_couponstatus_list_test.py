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
    request = sender.get("/api/rest/webmaster/json/couponstatus?")
    jsondump = request.json()
    code = request.status_code


def test_api_couponstatus_list_json_status():
    assert code == 200


def test_api_couponstatus_list_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def test_api_couponstatus_list_json():
    data = jsondump['data']

    assert any(names['name'] == 'Ожидаемые' for names in data) is True
    assert any(names['name'] == 'Активные' for names in data) is True
    assert any(names['name'] == 'Истекающие' for names in data) is True
    assert any(names['name'] == 'Новые' for names in data) is True
    assert any(names['name'] == 'Завершенные' for names in data) is True
    assert any(names['name'] == 'Эксклюзивные' for names in data) is True

    assert any(names['id'] == '0' for names in data) is True
    assert any(names['id'] == '1' for names in data) is True
    assert any(names['id'] == '2' for names in data) is True
    assert any(names['id'] == '3' for names in data) is True
    assert any(names['id'] == '4' for names in data) is True
    assert any(names['id'] == '5' for names in data) is True

    assert len(data) > 5
    for item in data:
        assert len(str(item['id'])) > 0
        assert len(item['name']) > 0


















