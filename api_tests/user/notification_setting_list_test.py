from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/notificationsettinglist?")
    jsondump = request.json()
    code = request.status_code


def test_notification_setting_list_json_status():
    assert code == 200


def test_notification_setting_list_json():
    items = jsondump['data']['items']
    assert len(items) > 5
    assert any(item['news_category_name'] == 'Новости CityAds' for item in items) is True
    assert any(item['news_category_name'] == 'Запуск новых офферов' for item in items) is True
    assert any(item['news_category_name'] == 'Возобновление работы офферов' for item in items) is True
    assert any(item['news_category_name'] == 'Улучшение условий работы с офферами' for item in items) is True
    assert any(item['news_category_name'] == 'Изменение условий работы с офферами' for item in items) is True
    assert any(item['news_category_name'] == 'Новые промо-материалы' for item in items) is True
    assert any(item['news_category_name'] == 'Акции и конкурсы' for item in items) is True


def test_notification_setting_list_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"















