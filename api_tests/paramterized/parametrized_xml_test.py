import pprint
import pytest
from sender.request_sender import Sender
from xml.etree import ElementTree as et

@pytest.mark.parametrize("url", [
    "/api/rest/webmaster/xml/offers/web/1/5?",
    "/api/rest/webmaster/xml/offers/web/1/5/id?",
    "/api/rest/webmaster/xml/offers/web/1/5/id?",
    "/api/rest/webmaster/xml/offers/web/1/5/name?",
    "/api/rest/webmaster/xml/offers/web/1/5/rating?",
    "/api/rest/webmaster/xml/offers/web/1/5/cpl?",
    "/api/rest/webmaster/xml/offers/web_favourite/1/5/cpa?",
    "/api/rest/webmaster/xml/offers/web_favourite/1/5/epc7days?",
    "/api/rest/webmaster/xml/offers/web_favourite/1/5/epc90days?",
    "/api/rest/webmaster/xml/offers/web_favourite/1/5/epc90days/asc?",
    "/api/rest/webmaster/xml/offers/web_favourite/1/5/epc7days/desc?",
    "/api/rest/webmaster/xml/offers/mobile/1/5?",
    "/api/rest/webmaster/xml/offers/mobile/1/5/id?",
    "/api/rest/webmaster/xml/offers/mobile/1/5/id?",
    "/api/rest/webmaster/xml/offers/mobile/1/5/name?",
    "/api/rest/webmaster/xml/offers/mobile/1/5/rating?",
    "/api/rest/webmaster/xml/offers/mobile/1/5/cpl?",
    "/api/rest/webmaster/xml/offers/mobile_favourite/1/5/cpa?",
    "/api/rest/webmaster/xml/offers/mobile_favourite/1/5/epc7days?",
    "/api/rest/webmaster/xml/offers/mobile_favourite/1/5/epc90days?",
    "/api/rest/webmaster/xml/offers/mobile_favourite/1/5/epc90days/asc?",
    "/api/rest/webmaster/xml/offers/mobile_favourite/1/5/epc7days/desc?",
    "/api/rest/webmaster/xml/exchangeratelist?",
    "/api/rest/webmaster/xml/profile?",
    "/api/rest/webmaster/xml/promolist?",
    "/api/rest/webmaster/xml/timezonelist?",
    "/api/rest/webmaster/xml/geo-list/web?",
    "/api/rest/webmaster/xml/geo-list/mobile?",
    "/api/rest/webmaster/xml/offers-types-list?",
    "/api/rest/webmaster/xml/offers-categories-list/web?",
    "/api/rest/webmaster/xml/offers-categories-list/mobile?",
    "/api/rest/webmaster/xml/offers-traffictypes-list/web?",
    "/api/rest/webmaster/xml/offers-platforms-list?",
    "/api/rest/webmaster/xml/couponstatus?",
    "/api/rest/webmaster/xml/coupontypes?",
    "/api/rest/webmaster/xml/couponother?",
    "/api/rest/webmaster/xml/offer/4325?",
    "/api/rest/webmaster/xml/offertarget/4325?",
    "/api/rest/webmaster/xml/analytics-audience/cityads.ru/3?",
    "/api/rest/webmaster/xml/analytics-geo/cityads.ru/3?",
    "/api/rest/webmaster/xml/analytics-input-traffic/cityads.ru/6?",
    "/api/rest/webmaster/xml/analytics-outgoing-traffic/cityads.ru/12?",
    "/api/rest/webmaster/xml/analytics-similar-sites/cityads.ru?",
    "/api/rest/webmaster/xml/analytics-competitors/cityads.ru?",
    "/api/rest/webmaster/xml/coupons?",
    "/api/rest/webmaster/xml/coupons/1/5?",
    "/api/rest/webmaster/xml/coupons?start=0&offer=Elitdress&limit=10&geo=186&sort=id&sort_type=asc&",
    "/api/rest/webmaster/xml/coupons?start=0&offer=Elitdress&limit=10&geo=186&sort=id&",
    "/api/rest/webmaster/xml/coupons?start=0&offer=Elitdress&limit=10&geo=186&",
    "/api/rest/webmaster/xml/goods-categories-list/goods?",
    "/api/rest/webmaster/xml/goods-categories-list/marketplace?",
    "/api/rest/webmaster/xml/goods-brands-list/goods?",
    "/api/rest/webmaster/xml/goods-brands-list/marketplace?",
    "/api/rest/webmaster/xml/goods-currency-list?",
    "/api/rest/webmaster/xml/rotators?",
    "/api/rest/webmaster/xml/banners?",
    "/api/rest/webmaster/xml/banner-sizes-list?",
    "/api/rest/webmaster/xml/goods?",
    "/api/rest/webmaster/xml/goods/0/10/186/1477?",
    "/api/rest/webmaster/xml/postback-list?",
    "/api/rest/webmaster/xml/offer-links/4325?",
    "/api/rest/webmaster/xml/statistics-offers/action_id/2014-06-15/2014-06-20?date_type=order_upload&",
    "/api/rest/webmaster/xml/statistics-actions/type_actions/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-offers/action_id/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-segments/type_offers/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-actions/type_actions/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-rate/event_time_day/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-tools/tools2/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-entrypoints/points_types/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-sources/typesources/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-geo/language/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-behaviour/new_user/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-technologies/os_type/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-devices/device_type_id/2014-06-15/2014-06-20?",
    "/api/rest/webmaster/xml/statistics-technologies/os_type/2014-06-15/2014-06-20?"])
def test_xml_status(url):
    pp = pprint.PrettyPrinter()
    sender = Sender()
    request = sender.get(url)
    raw_xml = request.text
    pp.pprint(raw_xml)
    xml = et.fromstring(raw_xml)
    code = request.status_code
    status = int(xml.find('.//status').text)
    print('status : ' + str(status))
    assert status != 500
    assert code != 500
    assert (code == 200 or code == 204)














