'''现场考察'''
import unittest
import time
import page
from page.page_supplier_inspect import SupplierInspect
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierInspect(unittest.TestCase):
    driver = None
    supplierinspect = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(2)
        cls.supplierinspect = SupplierInspect(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_inspect(self):
        '''现场考察提交'''
        try:
            self.supplierinspect.page_supplier_inspect_submit(self.name,
               '张大头' ,'2020-01-05','2020-01-10','建国北路111号',r'C:\Users\Administrator\Pictures\QQ\4.png')
            result = self.supplierinspect.page_is_if_supplier_inspect_success()
            self.assertTrue(result)
        except Exception as e:
            self.supplierinspect.base_get_image()
            raise e
