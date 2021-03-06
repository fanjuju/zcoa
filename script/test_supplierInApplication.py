'''纳入申请提交'''
import unittest
import time
import page
from page.page_supplier_inapplication import SupplierInApplication
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierInApplication(unittest.TestCase):
    driver = None
    supplierinapplication = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(2)
        cls.supplierinapplication = SupplierInApplication(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_inapplication(self):
        '''纳入申请提交'''
        try:
            self.supplierinapplication.page_supplier_inapplication_submit(self.name)
            result = self.supplierinapplication.page_is_if_supplier_inapplication_success()
            self.assertTrue(result)
        except Exception as e:
            self.supplierinapplication.base_get_image()
            raise e
