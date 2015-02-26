__author__ = 's.lugovskiy'
import os

global apiurl
global key

apiurl = 'http://cityads.com'
baseUrl = 'http://cityads.com'
wm = 'me0i@mail.ru'
wmPw = '123698745'
key = '859da89ead6c6ae40bb4d8e51bae4771'
hub = 'http://10.8.15.52:4444/wd/hub'
multiselectpage = 'http://controls.team.sagl/multiselect'
testrail_post_api = 'http://testrail.team.sagl/'
testrail_runid = 6

config = {}
for key in ['apiurl', 'baseUrl', 'wm', 'wmPw', 'key', 'hub', 'multiselectpage', 'testrail_post_api', 'testrail_runid']:
    try:
        config[key] = os.environ[key]
    except Exception as e:
        pass

try:
    apiurl = config['apiurl']
except KeyError as e:
    apiurl = 'http://cityads.com'

try:
    baseUrl = config['baseUrl']
except KeyError as e:
    baseUrl = 'http://cityads.com'

try:
    wm = config['wm']
except KeyError as e:
    wm = 'me0i@mail.ru'

try:
    wmPw = config['wmPw']
except KeyError as e:
    wmPw = '123698745'

try:
    key = config['key']
except KeyError as e:
    key = '859da89ead6c6ae40bb4d8e51bae4771'

try:
    hub = config['hub']
except KeyError as e:
    hub = 'http://10.8.15.52:4444/wd/hub'

try:
    multiselectpage = config['multiselectpage']
except KeyError as e:
    multiselectpage = 'http://control.team.sagl/multiselect'

try:
    testrail_post_api = config['testrail_post_api']
except KeyError as e:
    testrail_post_api = 'http://testrail.team.sagl/'

try:
    testrail_runid = config['testrail_runid']
except KeyError as e:
    testrail_runid = '6'


print('setup from env. variables: ')
print(config)


