from sender.request_sender import Sender
import datetime


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/exchangeratelist?")
    jsondump = request.json()
    code = request.status_code


def test_exchangeratelist_json_status():
    assert code == 200


def test_exchangeratelist_json():
    items = jsondump['data']['items']
    assert len(items) > 25
    for item in items:
        assert len(item['date']) > 0

    # #date check
    # today = datetime.datetime.now().strftime('%Y-%m-%d')
    # tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # assert (jsondump['data']['items'][1]['date']) == today
    # assert (jsondump['data']['items'][0]['date']) == tomorrow


def test_exchangeratelist_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















