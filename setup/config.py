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
multiselectpage = 'http://controls.duser020.test/controls/multiselect'
testrail_post_api = 'http://testrail.team.sagl/'
testrail_runid = 6

config = {}
for key in ['apiurl', 'baseUrl', 'wm', 'wmPw', 'key', 'hub', 'multiselectpage', 'testrail_post_api', 'testrail_runid']:
    config[key] = os.environ[key]

if config['apiurl']:
    apiurl = config['apiurl']
else:
    apiurl = 'http://cityads.com'

if config['baseUrl']:
    baseUrl = config['baseUrl']
else:
    baseUrl = 'http://cityads.com'

if config['wm']:
    wm = config['wm']
else:
    wm = 'me0i@mail.ru'

if config['wmPw']:
    wmPw = config['wmPw']
else:
    wmPw = '123698745'

if config['key']:
    key = config['key']
else:
    key = '859da89ead6c6ae40bb4d8e51bae4771'

if config['hub']:
    hub = config['hub']
else:
    hub = 'http://10.8.15.52:4444/wd/hub'

if config['multiselectpage']:
    multiselectpage = config['multiselectpage']
else:
    multiselectpage = 'http://controls.duser020.test/controls/multiselect'

if config['testrail_post_api']:
    testrail_post_api = config['testrail_post_api']
else:
    testrail_post_api = 'http://testrail.team.sagl/'

if config['testrail_runid']:
    testrail_runid = config['testrail_runid']
else:
    testrail_runid = '6'


print('setup from env. variables: ')
print(config)


