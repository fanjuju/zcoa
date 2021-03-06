from base.base import Base
import page
from common.search_apply_condition import SearchApply
import time

class ApplySearchFunction(Base):
    # 点击供应商管理tap栏
    def page_click_supplier(self):
        self.base_click(page.page_click_supplier)

    # 选择供应商引入项
    def page_select_suppier_apply(self):
        self.base_click(page.page_select_suppier_apply)

    # 输入查询条件-供应商名称
    def page_input_supplier_name(self, name):
        SearchApply(self.driver).common_supplier_name(name)

    # 点击查询
    def page_click_search_button(self):
        SearchApply(self.driver).common_select_button()

    # 整个查询功能
    def common_applySearchFunction(self,name):
        self.page_click_supplier()
        time.sleep(2)
        self.page_select_suppier_apply()
        time.sleep(2)
        self.page_input_supplier_name(name)
        time.sleep(2)
        self.page_click_search_button()