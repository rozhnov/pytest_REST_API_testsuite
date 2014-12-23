import json
import os
import pprint
from jsonschema import validate
from sender.request_sender import Sender


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    pp = pprint.PrettyPrinter()
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/analytics-geo/cityads.ru/3?")
    jsondump = request.json()
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema.json", 'r').read())


def test_analytics_geo_json_status():
    assert code == 200


def test_analytics_geo_json_schema():
    validate(jsondump, schema)


def test_analytics_geo_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def teardown_module():
    print('teardown module ' + __name__)
    print('\n----------------------------------------------------------------------\n')













