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
    sender = Sender()

    # NEW API (POST)
    # params = {"precision" : "min",
    #           "amount" : "90",
    #           "filters": [],
    #           "fields" : [
    #               "hit", "back_url" , "action_id"
    #           ]}
    #send request
    #request = sender.post_without_token("/monitor/rtstat/table", params)

    request = sender.get("/monitor/rtstat/table?precision=min&amount=90&metrics[]=hit&metrics[]=backurl&metrics[]=action_id")
    jsondump = request.json()
    code = request.status_code

    #print response
    pp = pprint.PrettyPrinter()
    print('response: ')
    pp.pprint(jsondump)

    #load schema for validation
    curdir = os.path.dirname(__file__)
    schema = json.loads(open(curdir + "/schema_table.json", 'r').read())


def test_realtime_table_schema():
    validate(jsondump, schema)


def test_realtime_table_status():
    status = jsondump['status']
    assert status == "ok"
    assert code == 200














