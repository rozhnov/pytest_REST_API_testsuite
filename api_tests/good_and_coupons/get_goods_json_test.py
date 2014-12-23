from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/goods?")
    jsondump = request.json()
    code = request.status_code


def test_get_goods_json_status():
    assert code == 200


def test_get_goods_json():
    goods = jsondump['data']['items']

    assert len(goods) == 50

    for key, value in goods.items():

        assert len(str(value['offer_name'])) > 0
        assert len(str(value['offer_id'])) > 0
        assert len(str(value['price'])) > 0
        assert len(str(value['region'])) > 0
        assert len(str(value['brand'])) > 0
        assert len(str(value['update_date'])) > 0
        assert len(str(value['url'])) > 0
        assert len(str(value['similarGoods'])) > 0
        assert 'http' in value['image']


def test_get_goods_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















