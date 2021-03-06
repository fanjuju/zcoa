import unittest
import time
import page
from page.page_supplier_apply_process import SupplierApplyProcess
from tool.driver import GetDriver


class TestSupplierProcess(unittest.TestCase):
    driver = None
    supplierprocess = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.supplierprocess = SupplierApplyProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_apply_process(self):
        '''供方开拓审核'''
        self.supplierprocess.page_supplier_process("该供应商资质良好，同意办理审核")
        result = self.supplierprocess.page_is_if_process_success()
        self.assertTrue(result)