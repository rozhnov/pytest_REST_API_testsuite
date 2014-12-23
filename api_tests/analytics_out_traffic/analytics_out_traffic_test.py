from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/analytics-outgoing-traffic/aliexpress.com/3?")
    jsondump = request.json()
    code = request.status_code


def test_analytics_out_traffic_json_status():
    assert code == 200


def test_analytics_out_traffic_json():
    items = jsondump['data']
    assert len(items) > 0
    for item in items:
        assert 'http' in item['icon']
        assert len(item['domain']) > 0
        assert type(item['rank']) is int
        assert len(str(item['share'])) > 0
        assert len(str(item['change'])) > 0


def test_analytics_out_traffic_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















