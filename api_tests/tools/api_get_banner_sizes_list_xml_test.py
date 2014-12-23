from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint
from setup.helper import get_key_values_xml


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
    request = sender.get("/api/rest/webmaster/xml/banner-sizes-list?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_banners_sizes_list_status():
    assert code == 200


def test_banners_sizes_list_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_banners_sizes_list_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data')
    assert len(data) > 10

    for item in data:
        assert len(item.find('id').text) > 0
        assert 'x' in item.find('name').text
        assert len(item.find('name').text) > 0












