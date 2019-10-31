# coding=utf-8
import unittest
import mock

from ApacheLogAnalyzer.utils.http_utils import TitleManager

class TestHttpUtils(unittest.TestCase):
    """测试http_util模块."""

    def setUp(self):
        pass

    @mock.patch('requests.get')
    def test_fetch_title(self, request_get):
        class Resp(object):
            def __init__(self, data):
                self.content = data

        request_get.side_effect = [
            Resp(b'''<html><head><title>test header</title></head><body></body></html>''')
        ]

        expect_result = [
            'test header'
        ]

        TitleManager.fetch_title('127.0.0.1', '/1.html')
        title = TitleManager.get_title('/1.html')
        self.assertEqual(expect_result[0], title, '结果不符. 期望值：%s' %
                         expect_result[0])
