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
    request = sender.get("/api/rest/webmaster/xml/statistics-offers/action_id/2014-06-15/2014-06-20?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_statistic_offers_xml_status():
    assert code == 200


def test_statistic_offers_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_statistic_offers_xml_data():
    error = xml.find('.//error').text
    assert error is None

    status = int(xml.find('.//status').text)
    if status == 200:
        items = xml.find('.//data/items')
        assert len(items) > 0
        for item in items:
            assert len(str(item.find('eventTime').text)) > 0
            assert len(str(item.find('actionID').text)) > 0
            assert len(str(item.find('actionName').text)) > 0
            assert int(item.find('clickCount').text) >= 0
            assert int(item.find('clickUniqCount').text) >= 0
            assert int(item.find('commissionOpen').text) >= 0
            assert int(item.find('commissionApproved').text) >= 0
            assert int(item.find('commissionCancelled').text) >= 0
            assert int(item.find('commissionApproved').text) >= 0
            assert int(item.find('crTotal').text) >= 0
            assert int(item.find('ctr').text) >= 0
            assert int(item.find('ecpc').text) >= 0
            assert int(item.find('ecpm').text) >= 0
            assert int(item.find('arLeads').text) >= 0
            assert int(item.find('crLeads').text) >= 0
            assert int(item.find('leadsOpen').text) >= 0
            assert int(item.find('leadsApproved').text) >= 0
            assert int(item.find('leadsCancelled').text) >= 0
            assert int(item.find('saleOpen').text) >= 0
            assert int(item.find('saleApproved').text) >= 0
            assert int(item.find('saleCancelled').text) >= 0
            assert int(item.find('backUrlRedirectCount').text) >= 0
            assert int(item.find('arSales').text) >= 0
            assert int(item.find('crSales').text) >= 0
            assert int(item.find('showCount').text) >= 0
            assert int(item.find('arTotal').text) >= 0



















