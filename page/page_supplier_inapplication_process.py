from base.base import Base
import page
import time

from common.function_search_process_condition import DevelopSheetSearch


class SupplierInApplicationProcess(Base):
    # 点击我的审核tap栏
    def page_click_my_process(self):
        self.base_click(page.page_click_my_process)

    # 点击纳入申请审核
    def page_click_inapplication_process(self):
        self.base_click(page.page_inapplication_process_button)

    # 调用common模块中我的审核操作全流程
    def page_inapplication_process(self,name,value):
        DevelopSheetSearch(self.driver).common_processFunction(name,value)

    # 断言
    def page_if_is_exist_submit_success(self):
        msg = self.base_find_element(page.page_process_success)
        return msg


    # 开发联系单办理审核流程
    def page_supplier_inapplication(self,name,value):
        self.page_click_my_process()
        time.sleep(2)
        self.page_click_inapplication_process()
        time.sleep(1)
        self.page_inapplication_process(name,value)