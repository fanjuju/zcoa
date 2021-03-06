'''纳入申请'''
from base.base import Base
from common.function_searh_apply_condition import ApplySearchFunction
import page
import time

class SupplierInApplication(Base):
    # 调用common中的查询功能
    def page_search_supplier_inspect(self,name):
        ApplySearchFunction(self.driver).common_applySearchFunction(name)

    # 鼠标移到操作栏中的纳入申请上并完成点击
    def page_click_inapplication(self):
        self.base_js(page.page_inapplication_button)

    # 确定弹窗中的确定按钮
    def page_click_inapplication_confirm(self):
        self.base_click(page.page_inapplication_confirm)

    # 断言
    def page_is_if_supplier_inapplication_success(self):
        return self.base_if_is_exist(page.page_success_button)

    # 纳入申请提交流程
    def page_supplier_inapplication_submit(self,name):
        self.page_search_supplier_inspect(name)
        time.sleep(2)
        self.page_click_inapplication()
        time.sleep(1)
        self.page_click_inapplication_confirm()

