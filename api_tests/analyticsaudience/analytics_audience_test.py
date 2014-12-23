import pprint
from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/analytics-audience/aliexpress.com/3?")
    jsondump = request.json()
    code = request.status_code


def test_analytics_audience_json_status():
    assert code == 200


def test_analytics_audience_total_json():
    assert jsondump['error'] == ''


def test_analytics_audience_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json not 500"


def test_analytics_audience_promo_code():
    audience_reach = jsondump['data']['audience-reach']
    audience_startdate = jsondump['data']['audience-startdate']
    audience_time = jsondump['data']['audience-time']
    audience_pages = jsondump['data']['audience-pages']

    assert len(audience_reach) > 0
    assert len(audience_startdate) > 0

    for item in audience_reach:
        assert type(item) is int

    for item in audience_time:
        assert type(item) is float

    for item in audience_pages:
        assert type(item) is float