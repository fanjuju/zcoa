'''供应商资质'''
import unittest
import time
import page
from page.page_supplier_qualification import SupplierQualification
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver


class TestSupplierQualification(unittest.TestCase):
    driver = None
    supplierqualification = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(2)
        cls.supplierqualification = SupplierQualification(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_supplier_qualification(self):
        '''供应商资质提交'''
        self.supplierqualification.page_supplier_qualification_submit(self.name,'C:/Users/Administrator/Pictures/QQ/2.png',r'C:\Users\Administrator\Pictures\QQ\3.png')
        result = self.supplierqualification.page_is_if_supplier_qualifaication_success()
        self.assertTrue(result)