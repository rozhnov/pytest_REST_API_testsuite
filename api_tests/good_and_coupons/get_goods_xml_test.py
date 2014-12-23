from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global xml
    pp = pprint.PrettyPrinter()
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/xml/goods?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_get_goods_list_xml_status():
    assert code == 200


def test_get_goods_list_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_get_goods_list_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data/items')
    assert len(data) == 50
    for item in data:
        assert int(item.find('id').text) > 0
        assert int(item.find('offer_id').text) > 0
        assert int(item.find('price').text) >= 0
        assert int(item.find('old_price').text) >= 0
        assert int(item.find('_3mepc').text) >= 0
        assert int(item.find('_7depc').text) >= 0
        assert int(item.find('delivery').text) >= 0
        assert int(item.find('category_id').text) >= 0
        assert int(item.find('coupons').text) >= 0
        assert int(item.find('rating').text) >= 0
        assert int(item.find('credit').text) >= 0
        assert int(item.find('retargeting').text) >= 0
        assert int(item.find('upc').text) >= 0

        assert len(str(item.find('name').text)) > 0
        assert len(str(item.find('offer_name').text)) > 0
        assert len(str(item.find('category').text)) > 0
        assert len(str(item.find('brand').text)) > 0
        assert len(str(item.find('update_date').text)) > 0
        assert len(str(item.find('currency').text)) > 0
        assert len(str(item.find('image').text)) > 0
        assert len(str(item.find('url').text)) > 0

        assert 'http' in item.find('image').text















