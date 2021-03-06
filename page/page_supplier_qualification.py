'''供应商资质审核'''
from base.base import Base
import page
import time
from common.search_apply_condition import SearchApply


class SupplierQualification(Base):
    # 点击供应商管理tap栏
    def page_click_supplier(self):
        self.base_click(page.page_click_supplier)

    # 选择供应商引入项
    def page_select_suppier_apply(self):
        self.base_click(page.page_select_suppier_apply)

    # 输入查询条件-供应商名称
    def page_input_supplier_name(self,name):
        SearchApply(self.driver).common_supplier_name(name)

    # 点击查询
    def page_click_search_button(self):
        SearchApply(self.driver).common_select_button()

    # 鼠标移到操作栏中的详情页上并完成点击
    def page_click_detail(self):
        self.base_js(page.page_detail)

    # 点击资质信息明细进行上传
    def page_upload_qualification_details(self,filePath1):
        self.base_upload_file(page.page_qualification_details,filePath1)

    # 点击资质评估报告
    def page_upload_qualification_report(self,filePath2):
        self.base_upload_file(page.page_qualification_report,filePath2)

    #  点击提交审核
    def page_click_submit(self):
        self.base_click(page.page_click_submit)

    # 断言：判断是否有操作成功提示
    def page_is_if_supplier_qualifaication_success(self):
        return self.base_if_is_exist(page.page_success_button)

    # 组合业务
    def page_supplier_qualification_submit(self,name,filePath1,filePath2):
        self.page_click_supplier()
        time.sleep(2)
        self.page_select_suppier_apply()
        time.sleep(2)
        self.page_input_supplier_name(name)
        time.sleep(1)
        self.page_click_search_button()
        time.sleep(2)
        self.page_click_detail()
        time.sleep(2)
        self.page_upload_qualification_details(filePath1)
        time.sleep(2)
        self.page_upload_qualification_report(filePath2)
        time.sleep(2)
        self.page_click_submit()
