'''试方试料'''
from base.base import Base
from common.function_searh_apply_condition import ApplySearchFunction
import page
import time

class SupplierMaterialTest(Base):
    # 调用common中的查询功能
    def page_search_supplier_materialtest(self,name):
        ApplySearchFunction(self.driver).common_applySearchFunction(name)

    # 鼠标移到操作栏中的详情页上并完成点击
    def page_click_detail(self):
        self.base_js(page.page_detail)

    # 点击试方试料tap栏
    def page_click_materialtest(self):
        self.base_click(page.page_materialtest)

    # 勾选试料类型
    def page_click_material_appliy(self):
        self.base_js(page.page_material_finish)

    # 输入评审意见
    def page_input_idea(self,idea):
        self.base_input(page.page_idea,idea)

    # 上传附件报告
    def page_upload_material_report(self,filePath):
        self.base_upload_file(page.page_material_report,filePath)

    # 点击提交审核
    def page_click_submit_button(self):
        self.base_click(page.page_click_submit)

    # 断言
    def page_is_if_submit_success(self):
        return self.base_find_element(page.page_success_button)

    # 试方试料提交审核流程
    def page_supplier_materialtest_submit(self,name,idea,filePath):
        self.page_search_supplier_materialtest(name)
        time.sleep(2)
        self.page_click_detail()
        time.sleep(2)
        self.page_click_materialtest()
        time.sleep(1)
        self.page_click_material_appliy()
        time.sleep(1)
        self.page_input_idea(idea)
        time.sleep(2)
        self.page_upload_material_report(filePath)
        time.sleep(1)
        self.page_click_submit_button()


