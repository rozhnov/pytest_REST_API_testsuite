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
    request = sender.get("/api/rest/webmaster/xml/notificationsettinglist?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_notification_setting_list_xml_status():
    assert code == 200


def test_notification_setting_list_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_notification_setting_list_xml_data():
    error = xml.find('.//error').text
    assert error is None

    data = xml.find('.//data/items')
    assert len(data) > 5

    assert any(item.find('news_category_name').text == 'Новости CityAds' for item in data) is True
    assert any(item.find('news_category_name').text == 'Запуск новых офферов' for item in data) is True
    assert any(item.find('news_category_name').text == 'Возобновление работы офферов' for item in data) is True
    assert any(item.find('news_category_name').text == 'Улучшение условий работы с офферами' for item in data) is True
    assert any(item.find('news_category_name').text == 'Изменение условий работы с офферами' for item in data) is True
    assert any(item.find('news_category_name').text == 'Новые промо-материалы' for item in data) is True
    assert any(item.find('news_category_name').text == 'Акции и конкурсы' for item in data) is True
    assert any(item.find('news_category_name').text == 'Новости CityAds (cityads.com)' for item in data) is True

    for item in data:
        assert len(item.find('news_category_id').text) > 0
        assert len(item.find('news_category_name').text) > 0
        assert len(item.find('status').text) > 0











