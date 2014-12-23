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
    request = sender.get("/api/rest/webmaster/xml/coupons?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_get_coupons_list_xml_status():
    assert code == 200


def test_get_coupons_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_get_coupons_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data/items')
    assert len(data) == 50
    for item in data:

        assert len(str(item.find('name').text)) > 0
        assert len(str(item.find('description').text)) > 0
        assert len(str(item.find('start_date').text)) > 0
        assert len(str(item.find('active_to').text)) > 0
        assert len(str(item.find('coupon_type').text)) > 0
        assert len(str(item.find('promo_code').text)) >= 0
        assert len(str(item.find('offer_name').text)) > 0
        assert len(str(item.find('offer_id').text)) > 0
        assert len(str(item.find('status').text)) > 0
        assert len(str(item.find('status').text)) > 0
        assert len(str(item.find('action_category_name').text)) > 0
        assert len(str(item.find('retargeting').text)) > 0
        assert len(str(item.find('retargeting').text)) > 0
        assert 'http' in item.find('image').text
        assert 'http' in item.find('url').text
        assert 'http' in item.find('url_frame').text















