'''现场考察'''
from base.base import Base
from common.function_searh_apply_condition import ApplySearchFunction
import page
import time

class SupplierInspect(Base):
    # 调用common中的查询功能
    def page_search_supplier_inspect(self,name):
        ApplySearchFunction(self.driver).common_applySearchFunction(name)

    # 鼠标移到操作栏中的详情页上并完成点击
    def page_click_detail(self):
        self.base_js(page.page_detail)

    # 点击详情中的现场考察
    def page_click_insepct(self):
        self.base_click(page.page_insepct)

    # 输入考察人员姓名
    def page_input_inspect_name(self,inspect_name):
        self.base_input(page.page_insepct_name,inspect_name)

    # 点击考察性质选择框
    def page_click_inspect_property(self):
        self.base_click(page.page_insepct_property)

    # 选择考察性质
    def page_select_inspect_property(self):
        self.base_click(page.page_insepct_property_value)

    # # 点击考察开始时间选择框
    # def page_click_inspect_starttime(self):
    #     self.base_click(page.page_insepct_starttime)

    # 选择考察开始时间
    def page_select_inspect_starttime(self,start_time):
        self.base_update_time(page.page_js,page.page_insepct_starttime,start_time)

    # 点击考察结束时间选择框
    def page_click_inspect_endtime(self):
        self.base_click(page.page_insepct_endtime)


    # 选择考察结束时间
    def page_select_inspect_endtime(self,end_time):
        self.base_update_time(page.page_js,page.page_insepct_endtime,end_time)

    # 点击考察地点选择框
    def page_click_inspect_address(self):
        self.base_click(page.page_insepct_address)

    # 选择考察地点
    def page_select_inspect_address(self):
        self.base_click(page.page_insepct_address_province)
        time.sleep(2)
        self.base_click(page.page_insepct_address_city)
        time.sleep(1)
        self.base_click(page.page_insepct_address_area)
        time.sleep(1)

    # 填写详细地址
    def page_input_inspect_address(self,address):
        self.base_input(page.page_insepct_detailed_address,address)

    # 上传考察报告
    def page_upload_inspect_reports(self,filePath):
        self.base_upload_file(page.page_material_report,filePath)

    # 点击提交审核
    def page_click_submit_button(self):
        self.base_click(page.page_click_submit)

    # 断言
    def page_is_if_supplier_inspect_success(self):
        return self.base_if_is_exist(page.page_success_button)

    # 考察内容填写并提交
    def page_supplier_inspect_submit(self,name,inspect_name,start_time,end_time,address,filePath):
        self.page_search_supplier_inspect(name)
        time.sleep(2)
        self.page_click_detail()
        time.sleep(2)
        self.page_click_insepct()
        time.sleep(1)
        self.page_input_inspect_name(inspect_name)
        time.sleep(1)
        self.page_click_inspect_property()
        time.sleep(1)
        self.page_select_inspect_property()
        time.sleep(2)
        self.page_select_inspect_starttime(start_time)
        time.sleep(1)
        self.page_click_inspect_endtime()
        time.sleep(2)
        self.page_select_inspect_endtime(end_time)
        time.sleep(1)
        self.page_click_inspect_address()
        time.sleep(2)
        self.page_select_inspect_address()
        time.sleep(2)
        self.page_input_inspect_address(address)
        time.sleep(1)
        self.page_upload_inspect_reports(filePath)
        time.sleep(1)
        self.page_click_submit_button()



