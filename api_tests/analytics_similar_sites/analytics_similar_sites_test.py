from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/analytics-similar-sites/aliexpress.com?")
    jsondump = request.json()
    code = request.status_code


def test_analytics_similar_sites_json_status():
    assert code == 200


def test_analytics_similar_sites_json():
    items = jsondump['data']
    assert len(items) > 0
    for item in items:
        assert len(item['domain']) > 0
        assert '.' in item['domain']
        assert type(item['global-rank']) is int
        assert len(str(item['category'])) > 0


def test_analytics_similar_sites_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















