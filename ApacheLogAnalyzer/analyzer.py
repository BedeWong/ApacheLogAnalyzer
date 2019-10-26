# coding=utf-8

import os

from ApacheLogAnalyzer.cmd import user_options
from ApacheLogAnalyzer.parser.record import ApacheLogRecord
from ApacheLogAnalyzer.report import report


class Analyzer(object):
    """日志分析类."""

    def __init__(self):
        self.ops = user_options.get_useroptions()

        self.files = self.ops.files
        self.report_objs = report.parse_report_type(self.ops.report_type)

    def parse_record(self, record):
        """添加记录到 报告对象进行分析"""
        for report_obj in self.report_objs:
            report_obj.add_record(record)

    def output_result(self):
        for report_obj in self.report_objs:
            report_detail = report_obj.export_report()
            report_detail.output()

    def do_work(self):
        """

        :return:
        """
        for logfile in self.files:
            if not os.path.exists(logfile):
                print('日志文件：[%s] 不存在.' % logfile)
                continue

            with open(logfile, 'r') as f:
                for line in f:
                    record = ApacheLogRecord.from_line(line)
                    if record is None:
                        continue

                    self.parse_record(record)


def main():
    analyzer = Analyzer()

    analyzer.do_work()
    analyzer.output_result()


if __name__ == '__main__':
    main()