# coding=utf-8
import requests
import re


def get_title(uri):
    assert isinstance(uri, str)

    # url = 'http://%s%s' % (domain, uri)
    # print('fetch url title: url: %s' % url)
    # resp = requests.get(url)
    # data = resp.content

    # print('the repsonse: %s' % data)

    # reg = r'<title>(.*?)</title>'
    # result = re.search(reg, data.decode())
    # if not result:
    #     print('response has no title, data:%s' % data)
    #     return ''

    # return result.group(1)
