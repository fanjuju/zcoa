'''试方试料'''
import unittest
import time
import page
from page.page_supplier_materialtest import SupplierMaterialTest
from script.test_supplierApply import TestSupplierApply

from tool.driver import GetDriver

class TestSupplierMaterialTest(unittest.TestCase):
    driver = None
    suppliermaterialtest = None
    name = TestSupplierApply().name

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(2)
        cls.suppliermaterialtest = SupplierMaterialTest(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    # 试方试料提交
    def test_supplier_materialtest(self):
        '''试方试料提交'''
        try:
            self.suppliermaterialtest.page_supplier_materialtest_submit(self.name,"批试审查合格",r'C:\Users\Administrator\Pictures\QQ\1178109511.jpg')
            time.sleep(1)
            self.assertIn("操作成功",self.suppliermaterialtest.base_page_source())
        except Exception as e:
            self.suppliermaterialtest.base_get_image()
            raise e