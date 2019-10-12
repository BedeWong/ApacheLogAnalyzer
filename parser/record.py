# coding=utf-8

import re


class RecordBase(object):
    """保存一条记录."""
    def __init__(self):
        self.data = {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    @classmethod
    def from_line(cls, line):
        raise NotImplementedError


class ApacheLogRecord(RecordBase):
    """apache 日志记录类，描述每条日志的基本构成"""

    # 匹配记录的正则规则
    REG_RULE = re.compile(r'(?P<remote_ip>\d+\.\d+\.\d+\.\d+) - -\s+' \
                          r'\[(?P<datetime>\S+\s\S+)\]\s+' \
                          r'"(?P<method>\w+)\s+' \
                          r'(?P<uri>\B/[-A-Za-z0-9+&@#/%?=~_|!:,.;]*)\s+' \
                          r'(?P<protocol>HTTP\S+)"\s+' \
                          r'(?P<code>\d+)\s' \
                          r'(?P<content_length>\d+)')

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_line(cls, line):
        assert isinstance(line, str)

        match_res = cls.REG_RULE.match(line)
        # 该行日志不是用户访问记录的日志
        if not match_res:
            return None

        result = match_res.groupdict(default='')
        return cls(result)


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