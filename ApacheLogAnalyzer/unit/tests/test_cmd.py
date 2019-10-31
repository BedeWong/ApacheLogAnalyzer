# coding=utf-8
import unittest
import sys


class TestUserOptions(unittest.TestCase):
    """"""
    def setUp(self):
        pass

    def test_user_options(self):
        sys.argv.append('apache.log')
        sys.argv.append('--type=all')

        from ApacheLogAnalyzer.cmd import user_options
        ops = user_options.get_useroptions()
        def_domain = '200.200.1.35'
        def_outfile = './report.md'
        def_type = ['all']
        logfiles= ['apache.log']

        self.assertEqual(ops.domain, def_domain, '默认域名参数不匹配')
        self.assertEqual(ops.outfile, def_outfile, '默认输出文件参数不匹配')
        self.assertEqual(ops.report_type, def_type, '')
        self.assertEqual(ops.files, logfiles, '')
