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
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)
    pp = pprint.PrettyPrinter()
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/statistics-geo/language/2014-12-01/2014-12-20?")
    jsondump = request.json()
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema.json", 'r').read())

    print('Json schema for validation: ')
    pp.pprint(schema)
    print('response: ')
    pp.pprint(jsondump)


def test_statistic_geo_json_status():
    assert code == 200


def test_statistic_geo_error():
    assert jsondump['error'] is ''


def test_statistic_geo_json_schema():
    validate(jsondump, schema)


def test_statistic_geo_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"













