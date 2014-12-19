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
    request = sender.get("/api/rest/webmaster/json/statistics-actions/type_actions/2014-06-15/2014-06-20?")
    jsondump = request.json()
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema_action_types.json", 'r').read())

    print('Json schema for validation: ')
    pp.pprint(schema)
    print('response: ')
    pp.pprint(jsondump)


def test_statistic_actions_json_status():
    assert code, 200


def test_statistic_actions_error():
    assert jsondump['error'] is ''


# def test_statistic_actions_json_schema():
#     validate(jsondump, schema)


def test_statistic_actions_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"













