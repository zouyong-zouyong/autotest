'''
        整个工具/框架运行的入口的入口 
'''
import unittest
from utils.HTMLTestRunner import HTMLTestRunner   # 类的名字叫HTMLTestRunner

# 1.加载所有的测试用例
# 查找cass文件夹下面的所有test_开头。py文件结尾的py文件
# Class 里面的成员方法都必须是test_
testcases = unittest.defaultTestLoader.discover('cases','test_*.py')

# 2. 把测试用例 装在 测试套件 ：测试集
testsuite = unittest.TestSuite()
testsuite.addTests(testcases)

# 3. 运行所有的测试用例，并且生成测试报告
title = "测试报告"
descr = "测试报告的描述"
report = "./report/report.html"  # 生成测试报告的文件路径可以自定义位置  （）


with open(report ,"wb") as f:   # 创建或 覆盖 report执行的文件,再把这个文件的对象给 F 变量
    runner = HTMLTestRunner(stream=f,title=title,description=descr)  #初始化 HTMLTestRunner
    runner.run(testsuite)   # 使用run方法运行所有的测试

