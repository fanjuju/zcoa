'''试方试料审核'''
import unittest
import time
import page
from page.page_supplier_materialtest_process import SupplierMaterialTestProcess
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierMaterialTestProcess(unittest.TestCase):
    driver = None
    suppliermaterialtestprocess = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.suppliermaterialtestprocess = SupplierMaterialTestProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()


    def test_supplier_materialtest_process(self):
        '''试方试料审核'''
        try:
            self.suppliermaterialtestprocess.page_supplier_materialtest(self.name,"试方试料考核很顺利")
            time.sleep(1)
            self.assertIn("成功处理",self.suppliermaterialtestprocess.base_page_source())
        except Exception as e:
            self.suppliermaterialtestprocess.base_get_image()
            raise e