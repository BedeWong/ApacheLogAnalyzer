# coding=utf-8

import argparse


class UserOptions(object):
    """管理用户参数和配置."""
    def __init__(self):
        """"""
        parser = argparse.ArgumentParser()
        parser.add_argument("files", help='待分析的日志文件 file1.log [file2.log [...]]',
                            type=str, nargs='+')
        parser.add_argument("--type", help='描述报表类型 [all[,ip[, article[, full]]]]',
                            type=str, nargs='+', default=['all'])
        parser.add_argument("--domain", help='服务器域名', type=str, default='120.79.208.53:8000')
        parser.add_argument("--outpath", help='报表输出目录', type=str, default='./')

        options = parser.parse_args()
        self.files = options.files
        self.report_type = options.type
        self.domain = options.domain
        self.outpath = options.outpath


__useroptions = UserOptions()


def get_useroptions():
    return __useroptions


def main():
    options = UserOptions()

    print(options.domain)
    print(options.outpath)
    print(options.report_type)
    print(options.files)


if __name__ == '__main__':
    main()