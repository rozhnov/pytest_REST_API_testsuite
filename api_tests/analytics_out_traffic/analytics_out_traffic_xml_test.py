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
    request = sender.get("/api/rest/webmaster/xml/analytics-outgoing-traffic/aliexpress.com/3?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_analytics_out_traffic_xml_status():
    assert code == 200


def test_analytics_out_traffic_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_analytics_out_traffic_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data')
    assert len(data) > 0
    for item in data:
        assert 'http' in item.find('icon').text
        assert len(item.find('rank').text) > 0
        assert len(item.find('domain').text) > 0
        assert len(item.find('share').text) > 0










