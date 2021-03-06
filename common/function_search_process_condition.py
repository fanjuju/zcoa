'''我的审核模块中的列表搜索'''
from base.base import Base
import page
import time

from common.search_process_condition import SearchProcess


class DevelopSheetSearch(Base):
    # 点击待办理列表
    def page_task_list(self):
        self.base_click(page.page_task_list)

    # 输入供应商名称
    def page_process_supplier_name(self, name):
        SearchProcess(self.driver).common_process_supplier_name(name)

    # 点击查询
    def page_process_select_button(self):
        SearchProcess(self.driver).common_process_select_button()

    # 点击办理
    def page_select_qualification_supplier(self):
        self.base_js(page.page_qualification_apply)

    # 点击详情中的办理
    def page_click_apply(self):
        self.base_click(page.page_click_apply)

    # 勾选弹窗中的审核同意
    def page_select_process_pass(self):
        self.base_click(page.page_select_process_pass)

    # 输入审核说明信息
    def page_input_process_remark(self, value):
        self.base_input(page.page_input_process_remark, value)

    # 点击确定按钮
    def page_click_confirm(self):
        self.base_click(page.page_click_confirm)

    # 我的审核操作全流程
    def common_processFunction(self,name,value):
        self.page_task_list()
        time.sleep(3)
        self.page_process_supplier_name(name)
        time.sleep(2)
        self.page_process_select_button()
        time.sleep(2)
        self.page_select_qualification_supplier()
        time.sleep(2)
        self.page_click_apply()
        time.sleep(2)
        self.page_select_process_pass()
        time.sleep(2)
        self.page_input_process_remark(value)
        time.sleep(2)
        self.page_click_confirm()