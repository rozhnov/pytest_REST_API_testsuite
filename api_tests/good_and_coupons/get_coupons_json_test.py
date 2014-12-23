from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/coupons?")
    jsondump = request.json()
    code = request.status_code


def test_get_coupons_json_status():
    assert code == 200


def test_get_coupons_json():
    coupons = jsondump['data']['items']

    assert len(coupons) == 50

    for value in coupons:

        assert len(str(value['id'])) > 0
        assert len(str(value['name'])) > 0
        assert len(str(value['description'])) > 0
        assert len(str(value['active_to'])) > 0
        assert len(str(value['coupon_type'])) > 0
        assert len(str(value['promo_code'])) >= 0
        assert len(str(value['offer_id'])) > 0
        assert len(str(value['status'])) > 0
        assert len(str(value['category_id'])) > 0
        assert len(str(value['action_category_name'])) > 0
        assert len(str(value['retargeting'])) > 0
        assert len(str(value['rating'])) > 0
        assert len(str(value['look'])) > 0
        assert 'http' in value['url']
        assert 'http' in value['url_frame']
        assert 'http' in value['image']


def test_get_coupons_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















