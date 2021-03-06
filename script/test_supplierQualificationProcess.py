'''供应商资质审核'''
import unittest
import time
import page
from page.page_supplier_qualification_process import SupplierQualificationProcess
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierQualificationProcess(unittest.TestCase):
    driver = None
    supplierqualificationprocess = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_204)
        time.sleep(2)
        cls.supplierqualificationprocess = SupplierQualificationProcess(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_qualification_process(self):
        '''供应商资质审核'''
        self.supplierqualificationprocess.page_supplier_qualification(self.name,"该供应商资质良好，可以通过审批")
        result = self.supplierqualificationprocess.page_is_if_process_success()
        self.assertTrue(result)