# 项目运行的入口
import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 1.自动查找所有测试用例
testcase = unittest.defaultTestLoader.discover('case', 'test_*.py')

# 2.使用使用htmltestrunner自动运行所有的测试用例并且生成测试报告
title = '自动化测试报告'
descr = '荟熊天选后台管理系统'
filepath = './report/test.html'

with open(file=filepath, mode='wb') as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testcase)