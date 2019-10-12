# coding=utf-8

from abc import abstractmethod

from ApacheLogAnalyzer.parser.record import ApacheLogRecord


class ParserBehavior(object):
    """日志解析器行为"""
    @abstractmethod
    def has_characteristic(self, attr):
        """判断该条记录是否包含某种性质"""
        raise NotImplementedError


class ApacheLogRecordParser(object):
    """
    所有apache日志记录的特性分析类."

    包含一系列函数，每个函数处理判断record是否包含某种特性.
    """

    @staticmethod
    def get_suffix(uri):
        assert isinstance(uri, str)

        path = uri.split('?')[0]
        return path.split('.')[-1]

    @staticmethod
    def is_article(record):
        """是否是文章"""
        assert isinstance(record, ApacheLogRecord)

        uri = record.get('uri')
        suffix = ApacheLogRecordParser.get_suffix(uri)
        if suffix in ['htm', 'html', 'pdf', 'doc', 'docx']:
            return True

        return False


def main():
    pass


if __name__ == '__main__':
    main()