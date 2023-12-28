# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner

def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'Test*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':
    cases = get_test_cases('testcases')
    dir = os.getcwd()
    outfile = open(dir+"/report/testReport.html","w")
    # filename = 'report/testReport.html'  # 设置报告文件名
    # with open(filename, 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, report_title=u'Mobile Auto Demo Test')
    runner.run(cases)
