# coding=utf-8
from abc import abstractmethod
from collections import Iterable
import sys
import traceback

from ApacheLogAnalyzer.parser.record import ApacheLogRecord
from ApacheLogAnalyzer.utils import http_utils


class BaseReport(object):
    """"""
    def __init__(self):
        self.head = []
        self.title = '报告'
        self.model = {}

    @abstractmethod
    def _new_ceil(self):
        """新建一条数据行."""
        raise NotImplementedError

    @abstractmethod
    def add_record(self, record):
        """添加一条记录."""
        raise NotImplementedError

    @abstractmethod
    def gen_report_line(self):
        """生成报告数据行."""
        raise NotImplementedError

    def export_report(self):
        """导出报告记录."""
        datas = self.gen_report_line()
        return ReportDetail(self.title, self.head, datas)

    def reset(self):
        self.model.clear()


class FullReport(BaseReport):
    """"""
    def __init__(self):
        super(FullReport, self).__init__()
        self.title = '完整报告'
        self.head = ['URL', 'IP', '访问次数']

    def _new_ceil(self):
        return {'pv': 0}

    def add_record(self, record):
        """增加一条日志记录."""
        assert isinstance(record, ApacheLogRecord)

        uri = record.get('uri')
        ip = record.get('remote_ip')
        pk = (uri, ip)
        if pk not in self.model:
            self.model[pk] = self._new_ceil()

        self.model[pk]['pv'] += 1

    def gen_report_line(self):
        """生成报告数据行."""
        for pk, item in self.model.items():
            url, ip = pk
            pv = item['pv']
            yield [url, ip, str(pv)]


class IpReport(BaseReport):
    """"""
    def __init__(self):
        super(IpReport, self).__init__()
        self.title = 'IP报告'
        self.head = ['IP', '访问数', '访问文章数']

    def _new_ceil(self):
        return {'count': 0, 'articles': set()}

    def add_record(self, record):
        assert isinstance(record, ApacheLogRecord)

        ip = record.get('remote_ip')
        if ip not in self.model:
            self.model[ip] = self._new_ceil()

        self.model[ip]['count'] += 1
        if record.has_characteristic('article'):
            self.model[ip]['articles'].add(record.get('uri'))

    def gen_report_line(self):
        """生成报告数据行."""
        for ip, item in self.model.items():
            count = item['count']
            article_cnt = len(item['articles'])

            yield [ip, str(count), str(article_cnt)]


class ArticleReport(BaseReport):
    """"""
    def __init__(self):
        super(ArticleReport, self).__init__()
        self.title = '文章报告'
        self.head = ['URL', '标题', '访问人次', '访问ip数']

    def _new_ceil(self):
        return {'pv': 0, 'ips': set()}

    def add_record(self, record):
        assert isinstance(record, ApacheLogRecord)

        uri = record.get('uri')
        title = ''
        try:
            title = http_utils.TitleManager.get_title(uri)
        except Exception as e:
            traceback.print_exc()

        if uri not in self.model:
            self.model[uri] = self._new_ceil()

        self.model[uri]['title'] = title
        self.model[uri]['pv'] += 1
        self.model[uri]['ips'].add(record.get('ip'))

    def gen_report_line(self):
        """生成报告数据行."""
        for url, item in self.model.items():
            title = item['title']
            pv_cnt = item['pv']
            ip_cnt = len(item['ips'])

            yield [url, title, str(pv_cnt), str(ip_cnt)]


class ReportDetail(object):
    """
    输出报告.

    用来渲染报告数据.
    """

    def __init__(self, title, heads, datas):
        self.heads = heads
        self.datas = datas
        self.title = title

    def output(self, file=None):
        if not isinstance(self.heads, (tuple, list)):
            raise ValueError()
        if not isinstance(self.datas, Iterable):
            raise ValueError()

        if not file:
            file = sys.stdout

        # 头部
        file.write('## %s\n' % self.title)
        file.write('|%s|\n' % ('|'.join(self.heads)))
        size = len(self.heads)
        file.write('|%s\n' % (':---:|' * size))

        # 数据部分
        for line in self.datas:
            file.write('|%s|\n' % ('|'.join(line)))

        file.write('\n')


# 所有的样式
REPORT_STYLE_CLASSES = {
    'full': FullReport,
    'ip': IpReport,
    'article': ArticleReport,
}


def parse_report_type(kinds):
    assert isinstance(kinds, (list, str))

    result = []

    if isinstance(kinds, str):
        kinds = [kinds,]

    if 'all' in kinds:
        for _, style_cls in REPORT_STYLE_CLASSES.items():
            result.append(style_cls())
        return result

    for item in kinds:
        style_cls = REPORT_STYLE_CLASSES[item]
        result.append(style_cls())

    return result
