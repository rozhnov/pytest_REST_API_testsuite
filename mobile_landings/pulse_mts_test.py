import pytest
import requests


urls = [
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=N',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=N'
]


@pytest.mark.parametrize("url", [
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=N',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=1',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=2',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=3',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=4',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=5',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=6',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=7',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=8',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=10',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=11',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=12',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=15',
    'http://pulse.mts.ru/landing/?id=56e9fd7f-fb7a-4d6e-b3e0-4834cb06b293&channel=13222178&section=maxipulse&lid=16',
])
def test_mobile_landings_response_status(url):
    r = requests.get(url)
    response_code = r.status_code
    content_type = r.headers['content-type']
    print('\n------------------------------------------------------------------')
    print('GET ' + r.url)
    print(response_code)
    print(content_type)

    div_count = r.text.count("div")
    print('div found in html: ' + str(div_count))
    assert response_code, 200
    assert content_type is not ''
    assert content_type is not None
    assert 'html' in content_type
    assert div_count > 0














