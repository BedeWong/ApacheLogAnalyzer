# coding=utf-8
import requests
import re
import traceback
import json


class TitleManager(object):
    """"""

    CACHE_FILE = './.titlecache'
    instance = None

    def __init__(self):
        self.data = {}
        self.load()

    def save(self):
        """"""
        try:
            with open(TitleManager.CACHE_FILE, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception:
            print('[ERR] 写入标题缓存文件失败！ file: %s' %
                  TitleManager.CACHE_FILE)
            traceback.print_exc()

    def load(self):
        with open(TitleManager.CACHE_FILE, 'r') as f:
            self.data = json.load(f)

    def add_title(self, uri, title):
        assert isinstance(uri, str)
        assert isinstance(title, str)

        if uri not in self.data:
            self.data[uri] = title

    @classmethod
    def fetch_title(cls, domain, uri):
        assert isinstance(uri, str)

        if TitleManager.instance is None:
            TitleManager.instance = cls()

        url = 'http://%s%s' % (domain, uri)
        print('[DEBUG] fetch url title: url: %s' % url)
        try:
            resp = requests.get(url, timeout=3)
        except Exception:
            traceback.print_stack()
            return

        data = resp.content or b''

        print('[DEBUG] the repsonse: %s' % data)

        reg = r'<title>(.*?)</title>'
        result = re.search(reg, data.decode())
        if not result:
            print('[ERR] response has no title, data:%s' % data)
            return

        title = result.group(1)
        TitleManager.instance.add_title(uri, title)

    @classmethod
    def get_title(cls, uri):
        assert(isinstance(uri, str))

        if TitleManager.instance is None:
            TitleManager.instance = cls()

        title = TitleManager.instance.data.get(uri, None)
        if not title:
            print('[WARN] uri title not found. uri:%s' % uri)
            title = ''

        return title

    @classmethod
    def close(cls):
        if TitleManager.instance is None:
            return

        TitleManager.instance.save()
