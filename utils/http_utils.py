# coding=utf-8
import requests
import re


def get_title(domain, uri):
    assert isinstance(uri, str)
    assert isinstance(domain, str)

    url = 'http://%s%s' % (domain, uri)
    # print('fetch url title: url: %s' % url)
    resp = requests.get(url)
    data = resp.content

    # print('the repsonse: %s' % data)

    reg = r'<title>(.*?)</title>'
    result = re.search(reg, data.decode())
    if not result:
        print('response has no title, data:%s' % data)
        return ''

    return result.group(1)


def main():
    print(get_title('120.79.208.53:8000', '/1.html'))


if __name__ == '__main__':
    main()