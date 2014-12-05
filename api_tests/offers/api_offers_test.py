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
    request = sender.get("/api/rest/webmaster/json/offers/web?limit=2&")
    jsondump = request.json()
    #print('response: ')
    #pp.pprint(jsondump)
    code = request.status_code
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema.json", 'r').read())
    #^.*\b(id)\b.*$ regexp for schema
    #print('json schema loaded for validation: ')
    #pp.pprint(schema)


def test_offers_json_status():
    assert code, 200


def test_offers_json_schema():
    validate(jsondump, schema)


def test_offers_json_status_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"


def test_offers_geo():
    items = jsondump['data']['items']
    for key, value in items.items():
        geo = jsondump['data']['items'][key]['geo']
        for item in geo:
            ccode = item['code']
            assert ccode != ''
            assert ccode is not None
            assert ccode is not 'null'
            assert len(ccode) > 0


def teardown_module():
    print('teardown module ' + __name__)
    print('\n----------------------------------------------------------------------\n')













