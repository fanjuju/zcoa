'''供应商开发联系单'''
import unittest
import time
import page
from page.page_supplier_developsheet import SupplierDevelopSheet
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierDevelopSheet(unittest.TestCase):
    driver = None
    supplierdevelopsheet = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(2)
        cls.supplierdevelopsheet = SupplierDevelopSheet(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_developSheet(self):
        '''供应商开发联系单提交'''
        self.supplierdevelopsheet.page_supplier_qualificationdevelopsheet_submit(self.name,
           '开发联系单试验' ,'检验是否符合标准','试验内容随机抽查','压根按照考核标准执行')
        result = self.supplierdevelopsheet.page_is_if_supplier_developsheet_success()
        self.assertTrue(result)