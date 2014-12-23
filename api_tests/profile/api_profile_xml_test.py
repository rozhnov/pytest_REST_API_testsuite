from sender.request_sender import Sender
from xml.etree import ElementTree as et
import re
import pprint


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global xml
    pp = pprint.PrettyPrinter()
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/xml/profile?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_profile_xml_status():
    assert code == 200


def test_profile_xml_status():
    status = xml.find('status')
    assert status != 500
    assert status is not ''
    assert status != 400


def test_profile_xml_data():
    user_id = xml.find('.//data/id').text
    email = xml.find('.//data/email').text
    assert user_id is not None
    assert user_id is not ''
    assert int(user_id) > 0
    assert len(email) > 0
    email_regexp = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    assert bool(email_regexp.match(email))


def teardown_module():
    print('teardown module ' + __name__)
    print('----------------------------------------------------------------------')













