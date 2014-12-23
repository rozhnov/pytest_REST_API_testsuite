from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/analytics-input-traffic/aliexpress.com/3?")
    jsondump = request.json()
    code = request.status_code


def test_analytics_traffic_json_status():
    assert code == 200


def test_analytics_traffic_json():
    traffic_volumes_startdate = jsondump['data']['traffic-volumes-startdate']
    social_volumes = jsondump['data']['search-volumes']
    search_volumes = jsondump['data']['social-volumes']
    mail_volumes = jsondump['data']['mail-volumes']
    paid_referrals_volumes = jsondump['data']['paid-referrals-volumes']
    direct_volumes = jsondump['data']['direct-volumes']
    referrals_volumes = jsondump['data']['referrals-volumes']
    appstore_internals_volumes = jsondump['data']['appstore-internals-volumes']

    assert traffic_volumes_startdate is not None
    assert len(traffic_volumes_startdate) > 0
    assert search_volumes is not None
    assert mail_volumes is not None
    assert paid_referrals_volumes is not None
    assert direct_volumes is not None
    assert referrals_volumes is not None
    assert appstore_internals_volumes is not None

    assert len(search_volumes) > 0
    for item in search_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0

    assert len(social_volumes) > 0
    for item in social_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0

    assert len(mail_volumes) > 0
    for item in mail_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0

    assert len(direct_volumes) > 0
    for item in direct_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0

    assert len(referrals_volumes) > 0
    for item in referrals_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0

    assert len(appstore_internals_volumes) > 0
    for item in appstore_internals_volumes:
        assert len(str((item['paid']))) > 0
        assert len(str(item['organic'])) > 0


def test_analytics_traffic_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"














