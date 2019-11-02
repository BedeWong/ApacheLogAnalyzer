# coding=utf-8
import unittest
import mock

from ApacheLogAnalyzer.utils.http_utils import TitleManager

class TestHttpUtils(unittest.TestCase):
    """测试http_util模块."""

    def setUp(self):
        with open('./.titlecache', 'w') as f:
            f.write('{}')

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

    @mock.patch('requests.get')
    def test_close(self, request_get):
        """测试文件保存."""
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
        TitleManager.close()

        title = TitleManager.get_title('/1.html')
        self.assertEqual(expect_result[0], title, '获取的标题匹配! ')

    @mock.patch('requests.get')
    def test_fetch_title_exception(self, request_get):
        """测试获取标题时异常."""
        request_get.side_effect = Exception
        TitleManager.fetch_title('127.0.0.1', '/2.html')
        self.assertEqual('', TitleManager.get_title('/2.html'), '获取的标题有误!')

    @mock.patch('json.dump')
    def test_save_to_file_exceptio(self, mock_json_dump):
        """测试写入文件失败."""
        mock_json_dump.side_effect = Exception
        if TitleManager.instance is None:
            TitleManager.instance = TitleManager()

        TitleManager.instance.add_title('/3.html', 'test3 title')
        self.assertRaises(Exception, TitleManager.close)
