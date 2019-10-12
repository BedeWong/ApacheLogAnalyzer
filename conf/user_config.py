# coding=utf-8

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--type", help='描述报表类型 [all[,ip[, article[, full]]]]',
                    type=str, nargs='+', default=['all'])
parser.add_argument("--domain", help='服务器域名', type=str, default='127.0.0.1')
parser.add_argument("--outpath", help='报表输出目录', type=str, default='./')


class UserOptions(object):
    """管理用户参数和配置."""
    def __init__(self):
        """"""
        options = self._parse_args()
        self.report_type = options.type
        self.domain = options.domain
        self.outpath = options.outpath

    @staticmethod
    def _parse_args():
        return parser.parse_args()


def main():
    options = UserOptions()

    print(options.domain)
    print(options.outpath)
    print(options.report_type)

if __name__ == '__main__':
    main()