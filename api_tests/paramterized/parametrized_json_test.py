import pprint
import pytest
from sender.request_sender import Sender
import time


@pytest.mark.parametrize("url", [
    "/api/rest/webmaster/json/offers/web/1/5?",
    "/api/rest/webmaster/json/offers/web/1/5/id?",
    "/api/rest/webmaster/json/offers/web/1/5/id?",
    "/api/rest/webmaster/json/offers/web/1/5/name?",
    "/api/rest/webmaster/json/offers/web/1/5/rating?",
    "/api/rest/webmaster/json/offers/web/1/5/cpl?",
    "/api/rest/webmaster/json/offers/web_favourite/1/5/cpa?",
    "/api/rest/webmaster/json/offers/web_favourite/1/5/epc7days?",
    "/api/rest/webmaster/json/offers/web_favourite/1/5/epc90days?",
    "/api/rest/webmaster/json/offers/web_favourite/1/5/epc90days/asc?",
    "/api/rest/webmaster/json/offers/web_favourite/1/5/epc7days/desc?",
    "/api/rest/webmaster/json/offers/mobile/1/5?",
    "/api/rest/webmaster/json/offers/mobile/1/5/id?",
    "/api/rest/webmaster/json/offers/mobile/1/5/id?",
    "/api/rest/webmaster/json/offers/mobile/1/5/name?",
    "/api/rest/webmaster/json/offers/mobile/1/5/rating?",
    "/api/rest/webmaster/json/offers/mobile/1/5/cpl?",
    "/api/rest/webmaster/json/offers/mobile_favourite/1/5/cpa?",
    "/api/rest/webmaster/json/offers/mobile_favourite/1/5/epc7days?",
    "/api/rest/webmaster/json/offers/mobile_favourite/1/5/epc90days?",
    "/api/rest/webmaster/json/offers/mobile_favourite/1/5/epc90days/asc?",
    "/api/rest/webmaster/json/offers/mobile_favourite/1/5/epc7days/desc?",
    "/api/rest/webmaster/json/exchangeratelist?",
    "/api/rest/webmaster/json/profile?",
    "/api/rest/webmaster/json/timezonelist?",
    "/api/rest/webmaster/json/geo-list/web?",
    "/api/rest/webmaster/json/geo-list/mobile?",
    "/api/rest/webmaster/json/offers-types-list?",
    "/api/rest/webmaster/json/offers-categories-list/web?",
    "/api/rest/webmaster/json/offers-categories-list/mobile?",
    "/api/rest/webmaster/json/offers-traffictypes-list/web?",
    "/api/rest/webmaster/json/offers-platforms-list?",
    "/api/rest/webmaster/json/couponstatus?",
    "/api/rest/webmaster/json/coupontypes?",
    "/api/rest/webmaster/json/couponother?",
    "/api/rest/webmaster/json/offer/4325?",
    "/api/rest/webmaster/json/offertarget/4325?",
    "/api/rest/webmaster/json/analytics-audience/cityads.ru/3?",
    "/api/rest/webmaster/json/analytics-geo/cityads.ru/3?",
    "/api/rest/webmaster/json/analytics-input-traffic/cityads.ru/6?",
    "/api/rest/webmaster/json/analytics-outgoing-traffic/cityads.ru/12?",
    "/api/rest/webmaster/json/analytics-similar-sites/cityads.ru?",
    "/api/rest/webmaster/json/analytics-competitors/cityads.ru?",
    "/api/rest/webmaster/json/coupons?",
    "/api/rest/webmaster/json/coupons/1/5?",
    "/api/rest/webmaster/json/coupons?start=0&offer=Elitdress&limit=10&geo=186&sort=id&sort_type=asc&",
    "/api/rest/webmaster/json/coupons?start=0&offer=Elitdress&limit=10&geo=186&sort=id&",
    "/api/rest/webmaster/json/coupons?start=0&offer=Elitdress&limit=10&geo=186&",
    "/api/rest/webmaster/json/goods-categories-list/goods?",
    "/api/rest/webmaster/json/goods-categories-list/marketplace?",
    "/api/rest/webmaster/json/goods-brands-list/goods?",
    "/api/rest/webmaster/json/goods-brands-list/marketplace?",
    "/api/rest/webmaster/json/goods-currency-list?",
    "/api/rest/webmaster/json/rotators?",
    "/api/rest/webmaster/json/banners?",
    "/api/rest/webmaster/json/banner-sizes-list?",
    "/api/rest/webmaster/json/goods?",
    "/api/rest/webmaster/json/goods/0/10/186/1477?",
    "/api/rest/webmaster/json/postback-list?",
    "/api/rest/webmaster/json/offer-links/4325?",
    "/api/rest/webmaster/json/statistics-offers/action_id/2014-12-01/2014-12-20?date_type=order_upload&",
    "/api/rest/webmaster/json/statistics-actions/type_actions/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-offers/action_id/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-segments/type_offers/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-actions/type_actions/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-rate/event_time_day/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-tools/tools2/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-entrypoints/points_types/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-sources/typesources/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-geo/language/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-behaviour/new_user/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-technologies/os_type/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-devices/device_type_id/2014-12-01/2014-12-20?",
    "/api/rest/webmaster/json/statistics-technologies/os_type/2014-12-01/2014-12-20?"])
def test_json_status(url):
    time.sleep(2)
    pp = pprint.PrettyPrinter()
    sender = Sender()
    request = sender.get(url)
    jsondump = request.json()
    pp.pprint(jsondump)
    code = request.status_code
    status = jsondump['status']
    print('status : ' + str(status))
    assert status != 500
    assert code != 500
    assert (code == 200 or code == 204)















