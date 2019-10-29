# coding=utf-8

import unittest
from io import StringIO

from ApacheLogAnalyzer.report.report import BaseReport
from ApacheLogAnalyzer.report.report import FullReport
from ApacheLogAnalyzer.report.report import IpReport
from ApacheLogAnalyzer.report.report import ArticleReport
from ApacheLogAnalyzer.report.report import parse_report_type
from ApacheLogAnalyzer.parser.record import ApacheLogRecord


class TestReport(unittest.TestCase):
    """"""

    def setUp(self):
        pass

    def test_add_recoed(self):
        full_report = FullReport()
        ip_report = IpReport()
        article_report = ArticleReport()

        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)

        full_report.add_record(record)
        ip_report.add_record(record)
        article_report.add_record(record)

        self.assertEqual(1, len(full_report.model), u'输据长度不符')
        self.assertEqual(1, len(ip_report.model), u'输据长度不符')
        self.assertEqual(1, len(article_report.model), u'输据长度不符')

        uri, ip = list(full_report.model.keys())[0]
        self.assertEqual('/index.htm', uri, u'uri数据错误')
        self.assertEqual('31.57.137.99', ip, u'ip数据错误')

    def test_export(self):
        full_report = FullReport()
        ip_report = IpReport()
        article_report = ArticleReport()

        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)

        full_report.add_record(record)
        ip_report.add_record(record)
        article_report.add_record(record)

        d1 = full_report.export_report()
        d2 = ip_report.export_report()
        d3 = article_report.export_report()

        self.assertEqual(1, len(d1.datas), u'数据长度不符')
        self.assertEqual(1, len(d2.datas), u'数据长度不符')
        self.assertEqual(1, len(d3.datas), u'数据长度不符')

    def test_output(self):
        full_report = FullReport()
        line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
        record = ApacheLogRecord.from_line(line)
        full_report.add_record(record)

        d1 = full_report.export_report()

        out = StringIO()
        d1.output(out)

        expect_val = '''|URL|IP|访问次数|
|:---:|:---:|:---:|
|/index.htm|31.57.137.99|1|
'''

        self.assertEqual(expect_val, out.getvalue(), '打印结果和预期不符, result:%s'
                         % out.getvalue())

    def test_parse_type(self):
        type = 'all'
        objs = parse_report_type(type)

        self.assertEqual(True, isinstance(objs, list), u'参数类型解析错误')

        for obj in objs:
            self.assertIsInstance(obj, BaseReport, u'数据类型错误')

        type = 'full'
        obj = parse_report_type(type)[0]
        self.assertIsInstance(obj, FullReport, u'解析对象出错')

        type = ['full', 'ip']
        obj = parse_report_type(type)[0]
        self.assertIsInstance(obj, FullReport, u'解析对象出错')

        obj = parse_report_type(type)[1]
        self.assertIsInstance(obj, IpReport, u'解析对象出错')
