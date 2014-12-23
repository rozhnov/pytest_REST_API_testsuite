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
    request = sender.get("/api/rest/webmaster/xml/couponstatus?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_couponsstatus_list_xml_status():
    assert code == 200


def test_couponsstatus_list_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_couponsstatus_list_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data')
    assert len(data) > 5

    assert any(item.find('name').text == 'Ожидаемые' for item in data) is True
    assert any(item.find('name').text == 'Активные' for item in data) is True
    assert any(item.find('name').text == 'Истекающие' for item in data) is True
    assert any(item.find('name').text == 'Новые' for item in data) is True
    assert any(item.find('name').text == 'Завершенные' for item in data) is True
    assert any(item.find('name').text == 'Эксклюзивные' for item in data) is True

    for item in data:
        assert len(item.find('id').text) > 0
        assert len(item.find('name').text) > 0











