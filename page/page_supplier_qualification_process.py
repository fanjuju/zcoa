'''供应商资质审核'''
from base.base import Base
import page
from common.search_process_condition import SearchProcess
import time

class SupplierQualificationProcess(Base):
    # 点击我的审核tap栏
    def page_click_my_process(self):
        self.base_click(page.page_click_my_process)

    # 点击资质审核按钮
    def page_qualification_process(self):
        self.base_click(page.page_qualification_process)

    # 点击待办理列表
    def page_task_list(self):
        self.base_click(page.page_task_list)

    # 输入供应商名称
    def page_process_supplier_name(self,name):
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
    def page_input_process_remark(self,value):
        self.base_input(page.page_input_process_remark,value)

    # 点击确定按钮
    def page_click_confirm(self):
        self.base_click(page.page_click_confirm)

    # 断言 判断是否有处理成功的提示语
    def page_is_if_process_success(self):
        return self.base_if_is_exist(page.page_process_success)

    # 组合业务
    def page_supplier_qualification(self,name,value):
        self.page_click_my_process()
        time.sleep(2)
        self.page_qualification_process()
        time.sleep(2)
        self.page_task_list()
        time.sleep(2)
        self.page_process_supplier_name(name)
        time.sleep(2)
        self.page_process_select_button()
        time.sleep(2)
        self.page_select_qualification_supplier()
        time.sleep(2)
        self.page_click_apply()
        time.sleep(1)
        self.page_select_process_pass()
        time.sleep(1)
        self.page_input_process_remark(value)
        time.sleep(1)
        self.page_click_confirm()
