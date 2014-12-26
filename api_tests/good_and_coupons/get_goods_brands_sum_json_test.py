from sender.request_sender import Sender


def test_get_goods_brands_sum_json():
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/goods?&brands=213,12894&")
    dump = request.json()
    total = dump['data']['total']
    request2 = sender.get("/api/rest/webmaster/json/goods?&brands=213&")
    dump2 = request2.json()
    total_brand213 = dump2['data']['total']
    request3 = sender.get("/api/rest/webmaster/json/goods?&brands=12894&")
    dump3 = request3.json()
    total_brand12894 = dump3['data']['total']
    total_brands_sum = total_brand213 + total_brand12894
    assert total == total_brands_sum

















