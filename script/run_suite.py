import unittest
import time


from TestRunner import SMTP, HTMLTestRunner

from script.test_supplierApplyProcess import TestSupplierProcess
from script.test_supplierApply import TestSupplierApply
from script.test_supplierDevelopSheetProcess import TestSupplierDevelopSheetProcess
from script.test_supplierDevelopSheet import TestSupplierDevelopSheet
from script.test_supplierInApplicationProcess import TestSupplierInApplicationProcess
from script.test_supplierInApplication import TestSupplierInApplication
from script.test_supplierInspectProcess import TestSupplierInspectProcess
from script.test_supplierInspect import TestSupplierInspect
from script.test_supplierMaterialTestProcess import TestSupplierMaterialTestProcess
from script.test_supplierMaterialTest import TestSupplierMaterialTest
from script.test_supplierQualificationProcess import TestSupplierQualificationProcess
from script.test_supplierQualification import TestSupplierQualification


# # 第一种方式
# # 获取当前时间
# from tool.HTMLTestRunner import HTMLTestRunner
#
# nowtime = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
# suite = unittest.defaultTestLoader.discover('script',pattern='test_*.py')
# report = '../reports' + '/' + nowtime + '_buy.html'
# with open(report,'wb') as f:
#     HTMLTestRunner(stream=f,title="采购系统测试报告",description="供应商管理模块测试用例执行").run(suite)
# # 发邮件功能
# smtp = SMTP(user="fjj@zhongcai.com", password="Fan123..", host="smtp.zhongcai.com")

# smtp.sender(to="fjj@zhongcai.com", subject="采购系统测试报告", attachments=report)



# 第三种方式：一个一个加进去执行
class TestSuite:
    def test_runsuite(self):
        # 获取当前时间
        nowtime = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

        # 创建一个测试套件
        suite = unittest.TestSuite()
        # 建立一个测试用例集,并添加到测试套件中
        suite.addTest(TestSupplierApply("test_supplier_apply"))
        suite.addTest(TestSupplierProcess("test_supplier_apply_process"))
        suite.addTest(TestSupplierQualification("test_supplier_qualification"))
        suite.addTest(TestSupplierQualificationProcess("test_supplier_qualification_process"))
        suite.addTest(TestSupplierDevelopSheet("test_supplier_developSheet"))
        suite.addTest(TestSupplierDevelopSheetProcess("test_supplier_developsheet_process"))
        suite.addTest(TestSupplierMaterialTest("test_supplier_materialtest"))
        suite.addTest(TestSupplierMaterialTestProcess("test_supplier_materialtest_process"))
        suite.addTest(TestSupplierInspect("test_supplier_inspect"))
        suite.addTest(TestSupplierInspectProcess("test_supplier_Inspect_process"))
        suite.addTest(TestSupplierInApplication("test_supplier_inapplication"))
        suite.addTest(TestSupplierInApplicationProcess("test_supplier_InApplication_process"))

        # 测试报告地址和显示格式配置
        report = '../reports' + '/' + nowtime + '_buy.html'
        with open(report,'wb') as f:
            # 创建一个运行对象runner，并运行套件中的测试用例
            runner = HTMLTestRunner(stream=f,verbosity = 2,title="采购系统测试报告",description="供应商管理模块测试用例执行")
            runner.run(suite)


        # 发邮件功能
        smtp = SMTP(user="fjj@zhongcai.com", password="Fan123..", host="smtp.zhongcai.com")
        smtp.sender(to="fjj@zhongcai.com",subject = "采购系统-供应商管理模块测试报告",attachments=report)

if __name__ == '__main__':
    unittest.main()

'''
# 第二种方式
if __name__ == '__main__':


# 获取当前时间
nowtime = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

# # 创建一个测试套件
# suite = unittest.TestSuite()
# # 建立一个测试用例集,并添加到测试套件中
# testcases = unittest.defaultTestLoader.discover('script',pattern='test_supplier_qualification.py')
# suite.addTests(testcases)
suite = unittest.defaultTestLoader.discover('script',pattern='test_supplierApply.py')

# 测试报告地址和显示格式配置
report = '../reports' + '/' + nowtime + '_buy.html'
with open(report,'wb') as f:
    # 创建一个运行对象runner，并运行套件中的测试用例
    runner = HTMLTestRunner(stream=f,verbosity = 2,title="采购系统测试报告",description="供应商管理模块测试用例执行")
    runner.run(suite)

# 发邮件功能
smtp = SMTP(user="fjj@zhongcai.com", password="Fan123..", host="smtp.zhongcai.com")
smtp.sender(to="fjj@zhongcai.com",subject = "采购系统测试报告",attachments=report)
'''
