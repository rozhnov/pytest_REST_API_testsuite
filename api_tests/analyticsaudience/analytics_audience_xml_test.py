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
    request = sender.get("/api/rest/webmaster/xml/analytics-audience/aliexpress.com/3?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_analytics_audience_xml_status():
    assert code == 200


def test_analytics_audience_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_analytics_audience_xml_data():
    error = xml.find('.//error').text
    assert error is None

    items = xml.find('.//data/audience-time')
    for item in items:
        assert len(item.text) > 0

    items = xml.find('.//data/audience-reach')
    assert len(items) > 0
    for item in items:
        assert len(item.text) > 0

    average_visits_per_day = xml.find('.//data/average/average_visits_per_day')
    assert len(average_visits_per_day.text) > 0

    average_time_on_site = xml.find('.//data/average/average_time_on_site')
    assert len(average_time_on_site.text) > 0

    average_page_views = xml.find('.//data/average/average_page_views')
    assert len(average_page_views.text) > 0

    average_bounce_rate = xml.find('.//data/average/average_bounce_rate')
    assert len(average_bounce_rate.text) > 0









