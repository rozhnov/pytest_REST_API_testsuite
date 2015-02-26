import json
import os
import pprint
import random
from jsonschema import validate
from sender.request_sender import Sender
import time


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global sender
    global rotator_name
    print('\n----------------------------------------------------------------------\n')
    print('setup module ' + __name__)

    # random data for rotator
    rotator_name = str(random.randint(1000, 9000))

    # POST parameters with random name
    params = {"name": rotator_name, "subaccount": "string", "type": "all", "add_new_offers": "1",
              "enable_optimization": "1"}
    # send request
    sender = Sender()
    request = sender.post("/api/rest/webmaster/json/rotator?", params)
    jsondump = request.json()

    #print response
    pp = pprint.PrettyPrinter()
    print('response: ')
    pp.pprint(jsondump)
    code = request.status_code
    curdir = os.path.dirname(__file__)

    #load schema for validation
    schema = json.loads(open(curdir + "/schema.json", 'r').read())


def test_rotators_json_status():
    assert code == 200


def test_rotators_json_schema():
    validate(jsondump, schema)


def test_rotators_json_status_400_or_500():
    status = jsondump['status']
    assert status != 500, "assert status in json  not 500"
    assert status != 400 , "assert status in json  not 400"


def test_rotators_id():
    banner_id = jsondump['data']['id']
    assert banner_id is not None
    assert banner_id is not ''
    time.sleep(15)
    rotator = sender.get('/api/rest/webmaster/json/rotator/' + str(banner_id) + '?').json()
    assert rotator['status'] is not 500
    assert rotator['data']['name'] == rotator_name


def teardown_module():
    print('teardown module ' + __name__)
    print('\n----------------------------------------------------------------------\n')













