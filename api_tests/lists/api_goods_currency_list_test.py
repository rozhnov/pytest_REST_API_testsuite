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
    sender = Sender()
    pp = pprint.PrettyPrinter()
    request = sender.get("/api/rest/webmaster/json/goods-currency-list?")
    jsondump = request.json()
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/currency_schema.json", 'r').read())
    print("\nresponse: ")
    pp.pprint(jsondump)


def test_api_currency_list_json_status():
    assert code == 200


def test_api_currency_list_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def test_api_currency_list_json_schema():
    validate(jsondump, schema)














