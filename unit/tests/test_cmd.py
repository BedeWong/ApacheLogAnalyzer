# coding=utf-8
import unittest
import sys


class TestUserOptions(unittest.TestCase):
    """"""
    def setUp(self):
        pass

    def test_user_options(self):
        sys.argv.append('apache.log')

        from ApacheLogAnalyzer.cmd import user_options
        ops = user_options.get_useroptions()
        def_domain = '120.79.208.53:8000'
        def_outpath = './'
        def_type = ['all']
        logfiles= ['apache.log']
        self.assertEqual(ops.domain, def_domain, '默认域名参数不匹配')
        self.assertEqual(ops.outpath, def_outpath, '默认域名参数不匹配')
        self.assertEqual(ops.report_type, def_type, '')
        self.assertEqual(ops.files, logfiles, '')