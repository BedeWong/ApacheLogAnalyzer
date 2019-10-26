# coding=utf-8
import unittest
import mock

class TestHttpUtils(unittest.TestCase):
    """测试http_util模块."""

    def setUp(self):
        pass

    @mock.patch('requests.get')
    def test_get_title(self, request_get):
        request_get.side_effect = [
            ''''''
        ]