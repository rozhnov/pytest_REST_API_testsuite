from sender.request_sender import Sender
import json
import os
import pprint
from jsonschema import validate


def setup():
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


def profile_json_status_test():
    assert code, 200


def profile_json_schema_test():
    validate(jsondump, schema)


def profile_json_status_500_test():
    status = jsondump['status']
    assert status != 500 , "assert status in json  not 500"


def teardown():
    print('teardown module ' + __name__)
    print('----------------------------------------------------------------------')













