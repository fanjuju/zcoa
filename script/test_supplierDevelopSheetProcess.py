'''供应商开发联系审核'''
import unittest
import time
import page
from page.page_supplier_developsheet_process import SupplierDevelopSheetProcess
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierDevelopSheetProcess(unittest.TestCase):
    driver = None
    supplierdevelopsheetprocess = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.supplierdevelopsheetprocess = SupplierDevelopSheetProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_developsheet_process(self):
        '''供应商开发联系审核'''
        try:
            self.supplierdevelopsheetprocess.page_supplier_developSheet(self.name,"开发联系单考核很顺利，可以通过考核")
            time.sleep(1)
            self.assertIn("成功处理",self.supplierdevelopsheetprocess.base_page_source)
        except Exception as e:
            self.supplierdevelopsheetprocess.base_get_image()
            raise e