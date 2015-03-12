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
    request = sender.get("/api/rest/webmaster/xml/statistics-geo/language/2014-12-01/2014-12-20?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_statistic_geo_xml_status():
    assert code == 200


def test_statistic_geo_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_statistic_geo_xml_data():
    error = xml.find('.//error').text
    assert error is None

    status = int(xml.find('.//status').text)
    if status == 200:
        items = xml.find('.//data/items')
        assert len(items) > 0
        for item in items:
            assert len(str(item.find('language').text)) > 0
            assert int(item.find('clickCount').text) >= 0
            assert int(item.find('clickUniqCount').text) >= 0
            assert float(item.find('commissionOpen').text) >= 0
            assert float(item.find('commissionApproved').text) >= 0
            assert float(item.find('commissionCancelled').text) >= 0
            assert float(item.find('commissionApproved').text) >= 0
            assert float(item.find('crTotal').text) >= 0
            assert float(item.find('ctr').text) >= 0
            assert float(item.find('ecpc').text) >= 0
            assert float(item.find('ecpm').text) >= 0
            assert int(item.find('arLeads').text) >= 0
            assert float(item.find('crLeads').text) >= 0
            assert int(item.find('leadsOpen').text) >= 0
            assert int(item.find('leadsApproved').text) >= 0
            assert int(item.find('leadsCancelled').text) >= 0
            assert int(item.find('saleOpen').text) >= 0
            assert int(item.find('saleApproved').text) >= 0
            assert int(item.find('saleCancelled').text) >= 0
            assert int(item.find('backUrlRedirectCount').text) >= 0
            assert len(item.find('arSales').text) >= 0
            assert len(item.find('crSales').text) >= 0
            assert int(item.find('showCount').text) >= 0
            assert len(item.find('arTotal').text) >= 0



















