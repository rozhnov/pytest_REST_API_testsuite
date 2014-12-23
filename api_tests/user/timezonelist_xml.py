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
    request = sender.get("/api/rest/webmaster/xml/timezonelist?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_timezonelist_status():
    assert code == 200


def test_timezonelist_status_xml():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_timezonelist_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data/items')
    assert len(data) > 200
    # assert any(item.find('name').text == 'Europe/Moscow' for item in data) is True












