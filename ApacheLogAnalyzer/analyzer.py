# coding=utf-8

from ApacheLogAnalyzer.cmd import user_options
from ApacheLogAnalyzer.parser.record import ApacheLogRecord
from ApacheLogAnalyzer.report import report


class Analyzer(object):
    """日志分析类."""

    def __init__(self):
        self.ops = user_options.get_useroptions()

        self.report_objs = report.parse_report_type(self.ops.report_type)

    def parse_record(self, record):
        """添加记录到 报告对象进行分析"""
        for report_obj in self.report_objs:
            report_obj.add_record(record)

    def output_result(self):
        for report_obj in self.report_objs:
            report_detail = report_obj.export_report()
            report_detail.output()

    def gen_lines(self):
        files = self.ops.files
        if not files:
            return

        for file in files:
            with open(file, 'r') as f:
                for line in f:
                    yield line

    def do_work(self):
        """

        :return:
        """
        lines = self.gen_lines()
        for line in lines:
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
