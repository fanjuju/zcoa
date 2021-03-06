'''新增供应商'''
import unittest
import time
import ddt
import page
from page.page_supplier_apply import SupplierApply
from tool.driver import GetDriver
from tool.readExcel import ReadExcel

# data = ReadExcel().get_excel()

# @ddt.ddt
class TestSupplierApply(unittest.TestCase):
    driver = None
    supplierapply = None
    name = "价格测试专用_一类_钙锌稳定剂"

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver(page.url_2090)
        time.sleep(3)
        # 实例化供应商引入新增页面
        cls.supplierapply = SupplierApply(cls.driver)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    #
    # def test_supplier_apply(self):
    #     '''供应商引入新增提交'''
    #     try:
    #         self.supplierapply.page_supplier_apply(self.name,"中财建材大世界","中财集团")
    #         time.sleep(1)
    #         value = self.supplierapply.page_success_button_is_exist()
    #         self.assertTrue(value,msg='新增一条供应商成功了')
    #     except Exception as e:
    #         self.supplierapply.base_get_image()
    #         raise e

    # @ddt.data(*data)
    # @ddt.unpack
    # 反向用例—必填项未填写
    def test_supplier_disapply(self):
        '''供应商引入新增提交异常'''
        try:
            self.supplierapply.page_supplier_apply(self.name, "供应商实力雄厚", "价格测试专用_一类_钙锌稳定剂")
            time.sleep(1)
            # self.assertIn(test_data["error_except"],self.supplierapply.base_page_source)
            value = self.supplierapply.page_success_button_is_exist()
            self.assertTrue(value, msg='新增一条供应商成功了')
        except Exception as e:
            self.supplierapply.base_get_image()
            raise e

if __name__ == '__main__':
    unittest.main()