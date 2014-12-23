from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint
from setup.helper import get_key_values_xml


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
    request = sender.get("/api/rest/webmaster/xml/goods-categories-list/goods?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_goods_categories_types_list_xml_status():
    assert code == 200


def test_goods_categories_types_list_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_goods_categories_types_list_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data')
    assert len(data) > 0

    ids = get_key_values_xml(data, 'id')
    yandex_category_ids = get_key_values_xml(data, 'yandex_category_id')

    names = get_key_values_xml(data, 'name')

    for iid in ids:
        assert len(iid) > 0

    for yandex_category_id in yandex_category_ids:
        assert len(yandex_category_id) > 0

    for name in names:
        assert len(name) > 0

    offers_count = get_key_values_xml(data, 'offers_count')
    for offercount in offers_count:
        assert int(offercount) > 0












