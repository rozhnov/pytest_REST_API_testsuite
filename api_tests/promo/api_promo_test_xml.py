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
    request = sender.get("/api/rest/webmaster/xml/promo/4325?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_promo_xml_status():
    assert code, 200


def test_promo_xml_status():
    status = xml.find('status')
    assert status is not 500
    assert status is not ''
    assert status is not 400


def test_promo_xml_data():
    total = xml.find('.//data/total').text
    assert int(total) > 0

    items = xml.find('.//data/items')
    print('PARSE')
    for item in items:
        assert '<script' in item.find('promo_code').text
        assert '<script' in item.find('promo_code_asynchron').text
        assert 'http' in item.find('file').text
        assert item.find('id') > 0


def teardown_module():
    print('teardown module ' + __name__)
    print('----------------------------------------------------------------------')













