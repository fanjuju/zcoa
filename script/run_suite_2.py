import unittest
import time
from unittestreport import TestRunner
# 第一种方式
# 获取当前时间
nowtime = time.strftime("%Y-%m-%d %H_%M_%S" ,time.localtime())
suite = unittest.defaultTestLoader.discover('script' ,pattern='test_*.py')
report = '../reports' + '/' + nowtime + '_buy.html'

runner = TestRunner(suite,filename=report ,title="采购系统测试报告" ,desc="供应商管理模块测试用例执行",tester = "fan",templates=1).run()


# 发邮件功能
runner.send_email(host="smtp.zhongcai.com", port=443, user="fjj@zhongcai.com", password="Fan123..", to_addrs="fjj@zhongcai.com")

runner = TestRunner(suite)
runner.run()

# smtp = SMTP(user="fjj@zhongcai.com", password="Fan123..", host="smtp.zhongcai.com")
# smtp.sender(to="fjj@zhongcai.com", subject="采购系统测试报告", attachments=report)