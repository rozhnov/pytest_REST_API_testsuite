import random
from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint
import time

def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global xml
    global pp
    global rotator_name
    pp = pprint.PrettyPrinter()
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)

    #create rotator

    rotator_name = str(random.randint(1000, 9000))
    post_params = "<createRotatorRequestData>" \
                  "<name>" + rotator_name + "</name>" \
                                            "<subaccount>string</subaccount>" \
                                            "<type>" \
                                            "all" \
                                            "</type>" \
                                            "<offers_included></offers_included>" \
                                            "<offers_excluded></offers_excluded>" \
                                            "<add_new_offers>" \
                                            "1" \
                                            "</add_new_offers>" \
                                            "<banner_sizes>" \
                                            "<item>240x400</item>" \
                                            "</banner_sizes>" \
                                            "<category_included></category_included>" \
                                            "<category_excluded></category_excluded>" \
                                            "<banners_included></banners_included>" \
                                            "<banners_excluded></banners_excluded>" \
                                            "<enable_optimization>1</enable_optimization>" \
                                            "</createRotatorRequestData>"
    sender = Sender()
    request = sender.post_xml("/api/rest/webmaster/xml/rotator?", params=post_params)
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_rotator_xml_status():
    assert code == 200


def test_rotator_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_rotator_xml_data():
    error = xml.find('.//error').text
    rotator_id = int(xml.find('.//data/id').text)
    assert rotator_id > 0
    assert error is None
    time.sleep(15)

    # get created rotator
    sender = Sender()
    response = sender.get('/api/rest/webmaster/xml/rotator/' + str(rotator_id) + '?')
    pp.pprint(response.text)
    get_rotator_xml = et.fromstring(response.text)
    get_rotator_code = response.status_code
    get_rotator_code_status = int(get_rotator_xml.find('.//status').text)
    banner_code = get_rotator_xml.find('.//data/code')

    assert get_rotator_code is not 500
    assert get_rotator_code_status == 200

    assert any(item.find('type').text == 'JS_CODE_ASYNC' for item in banner_code) is True
    assert any(item.find('type').text == 'JS_CODE' for item in banner_code) is True
    assert any(item.find('type').text == 'XML_FEED' for item in banner_code) is True

    assert any('script' in item.find('value').text for item in banner_code) is True
    assert any('get_xml' in item.find('value').text for item in banner_code) is True
    assert any('cityads.com' in item.find('value').text for item in banner_code) is True
    assert any('<script type="text/javascript">' in item.find('value').text for item in banner_code) is True

    #change created rotator (PUT)
    new_rotator_name = str(random.randint(1000, 9000))
    put_params = "<setRotatorRequestData>" \
                 "<id>" + str(rotator_id) + "</id>" \
                                            "<name>" + new_rotator_name + "</name>" \
                                                                          "<subaccount>string</subaccount>" \
                                                                          "<type>" \
                                                                          "all" \
                                                                          "</type>" \
                                                                          "<offers_included></offers_included>" \
                                                                          "<offers_excluded></offers_excluded>" \
                                                                          "<add_new_offers>" \
                                                                          "1" \
                                                                          "</add_new_offers>" \
                                                                          "<banner_sizes>" \
                                                                          "<item>240x400</item>" \
                                                                          "</banner_sizes>" \
                                                                          "<category_included></category_included>" \
                                                                          "<category_excluded></category_excluded>" \
                                                                          "<banners_included></banners_included>" \
                                                                          "<banners_excluded></banners_excluded>" \
                                                                          "<enable_optimization>1</enable_optimization>" \
                                                                          "</setRotatorRequestData>"
    response_put = sender.put_xml("/api/rest/webmaster/xml/rotator?", params=put_params)

    assert response_put.status_code != '500'
    assert et.fromstring(response_put.text).find('.//status') != '500'
    time.sleep(15)

    #get changed rotator
    response = sender.get('/api/rest/webmaster/xml/rotator/' + str(rotator_id) + '?')
    pp.pprint(response.text)
    get_rotator_xml = et.fromstring(response.text)
    get_rotator_name = get_rotator_xml.find('.//data/name').text
    get_rotator_code = response.status_code
    get_rotator_code_status = int(get_rotator_xml.find('.//status').text)

    assert get_rotator_code is not 500
    assert get_rotator_code_status == 200
    assert get_rotator_name == new_rotator_name





















