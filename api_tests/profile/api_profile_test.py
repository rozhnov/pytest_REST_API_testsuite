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
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/json/profile?")
    jsondump = request.json()
    pp.pprint(jsondump)
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema.json", 'r').read())
    #^.*\b(id)\b.*$ regexp for schema
    print('json schema loaded for validation: ')
    pp.pprint(schema)


def test_profile_json_status():
    assert code, 200


def test_profile_json_schema():
    validate(jsondump, schema)


def test_profile_json_status_500():
    status = jsondump['status']
    assert status != 500 , "assert status in json  not 500"


def teardown_module():
    print('teardown module ' + __name__)
    print('----------------------------------------------------------------------')













