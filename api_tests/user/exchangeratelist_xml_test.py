from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint
import datetime

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
    request = sender.get("/api/rest/webmaster/xml/exchangeratelist?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_exchangeratelist_xml_status():
    assert code == 200


def test_exchangeratelist_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_exchangeratelist_xml_data():
    error = xml.find('.//error').text
    assert error is None
    # today = datetime.datetime.now().strftime('%Y-%m-%d')

    # #date check
    # tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # assert xml.find('.//data/items/item[2]/date').text == today
    # assert xml.find('.//data/items/item[1]/date').text == tomorrow

    data = xml.find('.//data/items')
    assert len(data) > 25












