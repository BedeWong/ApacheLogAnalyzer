# coding=utf-8

import re

from .parser import ParserBehavior
from .parser import ApacheLogRecordParser


class RecordBase(object):
    """保存一条记录."""
    def __init__(self):
        self.data = {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    @classmethod
    def from_line(cls, line):
        raise NotImplementedError


class ApacheLogRecord(RecordBase, ParserBehavior):
    """apache 日志记录类，描述每条日志的基本构成"""

    # 匹配记录的正则规则
    REG_RULE = re.compile(r'(?P<remote_ip>\d+\.\d+\.\d+\.\d+) - -\s+' \
                          r'\[(?P<datetime>\S+\s\S+)\]\s+' \
                          r'"(?P<method>\w+)\s+' \
                          r'(?P<uri>\B/[-A-Za-z0-9+&@#/%?=~_|!:,.;]*)\s+' \
                          r'(?P<protocol>HTTP\S+)"\s+' \
                          r'(?P<code>\d+)\s' \
                          r'(?P<content_length>\d+)')
    # 资源文件列表
    RESOURCE_FILE_LIST = ['js', 'css', 'woff2', 'woff', 'ico']

    def __init__(self, data):
        super(ApacheLogRecord, self).__init__()

        self.data = data
        self.characteristic = dict()
        self.parser = ApacheLogRecordParser()

    def has_characteristic(self, attr):
        assert isinstance(attr, str)

        if attr in self.characteristic:
            return True

        judge_name = 'is_' + attr
        judge_func = getattr(self.parser, judge_name, None)
        if not judge_func:
            return False

        assert callable(judge_func)

        res = judge_func(self.data)
        if res:
            self.characteristic[attr] = True
        return res

    @classmethod
    def from_line(cls, line):
        assert isinstance(line, str)

        match_res = cls.REG_RULE.match(line)
        # 该行日志不是用户访问记录的日志行
        if not match_res:
            print('can not match line: %s, not a user access record' % line)
            return None

        result = match_res.groupdict(default='')
        uri = result.get('uri', None)
        if not uri:
            print('this line has no uri field. line %s' % line)
            return None

        if cls.is_resource_file(uri):
            print('this record is a resource file. record: %s' % result)
            return None

        return cls(result)

    @staticmethod
    def is_resource_file(uri):
        """
        判断uri对应的是不是资源文件.

        :param uri:  用户访问的地址
        :return: bool value
        """
        assert isinstance(uri, str)

        # 去掉参数部分
        path = uri.split('?')[0]
        suffix = path.split('.')[-1]
        if not suffix:
            print('this uri has no suffix uri: %s' % uri)
            # TODO..
            return None

        # 需要过滤的uri类型
        if suffix in ApacheLogRecord.RESOURCE_FILE_LIST:
            return True

        return False


def main():
    line = '''31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203 
31.57.137.99 - - [11/Aug/2019:05:00:21 +0800] "GET /index.htm HTTP/1.0" 200 3203'''
    record = ApacheLogRecord.from_line(line)
    print(record.data)
    '''
    output:
        {
            'remote_ip': '31.57.137.99',
            'datetime': '11/Aug/2019:05:00:21 +0800',
            'method': 'GET',
            'uri': '/index.htm',
            'protocol': 'HTTP/1.0',
            'code': '200',
            'content_length': '3203'
        }
    '''


if __name__ == '__main__':
    main()