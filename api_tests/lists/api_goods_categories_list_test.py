import json
import os
from jsonschema import validate
from sender.request_sender import Sender
from setup.helper import get_recurse_key_values_json


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/goods-categories-list/goods?")
    jsondump = request.json()
    code = request.status_code


def test_api_goods_categories_types_list_json_status():
    assert code == 200


def test_api_goods_categories_types_list_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def test_api_goods_categories_types_list_json():
    data = jsondump['data']

    #получаем все значения ключей во всех сложенных объекитах рекурсивно
    id_list = get_recurse_key_values_json([], data, 'id')
    yandex_category_id_list = get_recurse_key_values_json([], data, 'yandex_category_id')

    assert len(id_list) > 1000
    for goods_id in id_list:
        assert len(str(goods_id)) > 0

    assert len(yandex_category_id_list) > 1000
    for yandex_category_id in yandex_category_id_list:
        assert len(str(yandex_category_id)) > 0

    assert len(data) > 2
    for item in data:
        assert len(str(item['id'])) > 0
        assert len(item['parent_id']) > 0

















