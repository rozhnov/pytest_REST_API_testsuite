from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/timezonelist?")
    jsondump = request.json()
    code = request.status_code


def test_timezonelist_json_status():
    assert code == 200


def test_timezonelist_json():
    items = jsondump['data']['items']
    assert len(items) > 200
    # assert any(item['name'] == 'Europe/Moscow' for item in items) is True


def test_timezonelist_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















