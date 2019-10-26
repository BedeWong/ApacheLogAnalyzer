# coding=utf-8

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("files", help='待分析的日志文件 file1.log [file2.log [...]]',
                    type=str, nargs='+')
parser.add_argument("--type", help='描述报表类型 [all[,ip[, article[, full]]]]',
                    type=str, nargs='+', default=['all'])
parser.add_argument("--domain", help='服务器域名', type=str, default='120.79.208.53:8000')
parser.add_argument("--outpath", help='报表输出目录', type=str, default='./')


class UserOptions(object):
    """管理用户参数和配置."""
    def __init__(self):
        """"""
        options = self._parse_args()
        self.files = options.files
        self.report_type = options.type
        self.domain = options.domain
        self.outpath = options.outpath

    @staticmethod
    def _parse_args():
        return parser.parse_args()


useroptions = UserOptions()


def get_useroptions():
    return useroptions


def main():
    options = UserOptions()

    print(options.domain)
    print(options.outpath)
    print(options.report_type)
    print(options.files)


if __name__ == '__main__':
    main()