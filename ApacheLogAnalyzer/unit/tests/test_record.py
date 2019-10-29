# coding=utf-8
import unittest
import mock

from ApacheLogAnalyzer.parser.record import ApacheLogRecordParser
from ApacheLogAnalyzer.parser.record import ApacheLogRecord


class TestApacheLogRecordParser(unittest.TestCase):
    """"""

    def setUp(self):
        pass

    def test_get_suffix(self):
        """测试基本功能."""
        uris = [
            '/test/index.html',
            '/test/index',
            '/test',
            '/test/index.html?param=xx',
            '/test/index.html?param=xx&param2=yy',
            '/'
        ]

        expects = [
            'html', '', '', 'html', 'html', ''
        ]

        for idx, uri in enumerate(uris):
            res = ApacheLogRecordParser.get_suffix(uri)
            self.assertEqual(res, expects[idx], '%s 错误！, result=%s' %
                             (uri, res))

    def test_get_suffix_param_err(self):
        """测试参数类型错误."""
        self.assertRaises(AssertionError, ApacheLogRecordParser.get_suffix, b'12345')
        self.assertRaises(AssertionError, ApacheLogRecordParser.get_suffix, self)

    @mock.patch('ApacheLogAnalyzer.parser.record.RecordBase.get')
    def test_is_article(self, record):
        """测试 判断uri是否是文章类请求."""
        data_model = [
            '/test/index.html',
            '/test/index',
            '/test',
            '/test/index.html?param=xx',
            '/test/index.html?param=xx&param2=yy',
            '/',
            '/test/index.doc',
            '/test/index.pdf',
            '/test/index.docx',
            '/test/index.html',
            '/test/html'
        ]
        record.side_effect = data_model
        expects = [True, False, False, True, True,
                   False, True, True, True, True, False]

        obj = ApacheLogRecord({})
        for idx, expect in enumerate(expects):
            result = ApacheLogRecordParser.is_article(obj)
            self.assertEqual(expect, result,
                             'result=%s, uri=%s' % (expect, data_model[idx]))


class TestApacheLogRecord(unittest.TestCase):
    """apache 日志记录测试类."""
    def setUp(self):
        pass

    def test_ApacheLogRecord_usage(self):
        """测试基本使用."""
        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)

        self.assertEqual(True, record.has_characteristic('article'), 'expect value is True')

        uri = record.get('uri')
        self.assertEqual(False, ApacheLogRecord.is_resource_file(uri), 'expect value is False')

    def test_ApacheLogRecord_not_match_line(self):
        """测试日志不正确，匹配不到行."""
        line = '''0] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)
        self.assertIsNone(record, 'expect value is None, record:%s' % record)

    def test_ApacheLogRecord_is_resoure_file(self):
        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.ico HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)
        self.assertIsNone(record, 'expect value is None, record:%s' % record)

    def test_ApacheLogRecord_not_find_judge_func(self):
        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)
        ret = record.has_characteristic('test_not_find')
        self.assertEqual(False, ret, 'expect value is False, ret:%s' % ret)
