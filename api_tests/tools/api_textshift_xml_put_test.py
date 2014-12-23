import random
from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global xml
    global pp
    global text_shift_name
    global status
    pp = pprint.PrettyPrinter()
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)

    #create shift
    text_shift_name = str(random.randint(1000, 9000))
    post_params = '<createTextShiftRequestData>' \
                  '<name>' + text_shift_name + '</name> \
                        <subaccount>string</subaccount>\
                        <subaccount1>string</subaccount1>\
                        <subaccount2>string</subaccount2>\
                        <subaccount3>string</subaccount3>\
                        <subaccount4>string</subaccount4>\
                        <subaccount5>string</subaccount5>\
                        <links>on</links>\
                        <links_timeout>1000</links_timeout>\
                        <links_excluded_sites>string</links_excluded_sites>\
                        <text>on</text>\
                        <text_target>current</text_target>\
                        <text_excluded_sites>string</text_excluded_sites>\
                        <clickunder>on</clickunder>\
                        <clickunder_timeout>1000</clickunder_timeout>\
                        <clickunder_excluded_sites>string</clickunder_excluded_sites>\
                        <clickunder_scheme_first>0</clickunder_scheme_first>\
                        <clickunder_scheme_second>0</clickunder_scheme_second>\
                        <clickunder_scheme_third>0</clickunder_scheme_third>\
                        <clickunder_target>2</clickunder_target>\
                        </createTextShiftRequestData>'
    sender = Sender()
    request = sender.post_xml("/api/rest/webmaster/xml/textshift?", params=post_params)
    pp.pprint(request.text)
    code = request.status_code
    raw_xml = request.text
    xml = et.fromstring(raw_xml)
    shift_id = xml.find('.//data/id').text

    #change shift
    new_text_shift_name = str(random.randint(1000, 9000))
    put_params = '<setTextShiftRequestData>' \
                 '<id>' + shift_id + '</id>' \
                                     '<name>' + new_text_shift_name + '</name> \
                        <subaccount>string</subaccount>\
                        <subaccount1>string</subaccount1>\
                        <subaccount2>string</subaccount2>\
                        <subaccount3>string</subaccount3>\
                        <subaccount4>string</subaccount4>\
                        <subaccount5>string</subaccount5>\
                        <links>on</links>\
                        <links_timeout>1000</links_timeout>\
                        <links_excluded_sites>string</links_excluded_sites>\
                        <text>on</text>\
                        <text_target>current</text_target>\
                        <text_excluded_sites>string</text_excluded_sites>\
                        <clickunder>on</clickunder>\
                        <clickunder_timeout>1000</clickunder_timeout>\
                        <clickunder_excluded_sites>string</clickunder_excluded_sites>\
                        <clickunder_scheme_first>0</clickunder_scheme_first>\
                        <clickunder_scheme_second>0</clickunder_scheme_second>\
                        <clickunder_scheme_third>0</clickunder_scheme_third>\
                        <clickunder_target>2</clickunder_target>\
                        </setTextShiftRequestData>'
    request = sender.put_xml("/api/rest/webmaster/xml/textshift?", params=put_params)
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)
    status = int(xml.find('status').text)


def test_text_shift_xml_put_data():
    error = xml.find('.//error').text
    assert status != 500
    assert status != 400
    assert error is None
















