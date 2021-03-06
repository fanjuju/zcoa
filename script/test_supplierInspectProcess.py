'''现场考察'''
import unittest
import time
import page
from page.page_supplier_insepect_process import SupplierInspectProcess
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierInspectProcess(unittest.TestCase):
    driver = None
    supplierinspectprocess = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.supplierinspectprocess = SupplierInspectProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_Inspect_process(self):
        '''现场考察审核'''
        try:
            self.supplierinspectprocess.page_supplier_inspect(self.name,"现场考察合格")
            time.sleep(1)
            self.assertIn("成功处理",self.supplierinspectprocess.base_page_source)
        except Exception as e:
            self.supplierinspectprocess.base_get_image()
            raise e