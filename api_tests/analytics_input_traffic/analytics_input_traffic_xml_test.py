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
    request = sender.get("/api/rest/webmaster/xml/analytics-input-traffic/aliexpress.com/3?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_analytics_traffic_xml_status():
    assert code == 200


def test_analytics_traffic_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_analytics_traffic_xml_data():
    error = xml.find('.//error').text
    assert error is None

    social_volumes = xml.find('.//data/social-volumes')
    search_volumes = xml.find('.//data/search-volumes')
    mail_volumes = xml.find('.//data/mail-volumes')
    paid_referrals_volumes = xml.find('.//paid-referrals-volumes')
    direct_volumes = xml.find('.//data/direct-volumes')
    referrals_volumes = xml.find('.//data/referrals-volumes')
    appstore_internals_volumes = xml.find('.//data/appstore-internals-volumes')

    for item in social_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in paid_referrals_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in search_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in mail_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in direct_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in referrals_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0

    for item in appstore_internals_volumes:
        assert len(item.find('organic').text) > 0
        assert len(item.find('paid').text) > 0








