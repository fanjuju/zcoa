'''纳入申请审核'''
import unittest
import time
import page
from page.page_supplier_inapplication_process import SupplierInApplicationProcess
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver

class TestSupplierInApplicationProcess(unittest.TestCase):
    driver = None
    supplierinapplicationprocess = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.supplierinapplicationprocess = SupplierInApplicationProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_InApplication_process(self):
        '''纳入申请审核'''
        try:
            self.supplierinapplicationprocess.page_supplier_inapplication(self.name,"各项考核指标均正常")
            time.sleep(1)
            self.assertIn("成功处理",self.supplierinapplicationprocess.base_page_source)
        except Exception as e:
            self.supplierinapplicationprocess.base_get_image()
            raise e