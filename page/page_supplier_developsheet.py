from base.base import Base
from common.function_searh_apply_condition import ApplySearchFunction
import page
import time

class SupplierDevelopSheet(Base):
    # 调用common中的查询功能
    def page_search_supplier_developsheet(self,name):
        ApplySearchFunction(self.driver).common_applySearchFunction(name)

    # 鼠标移到操作栏中的详情页上并完成点击
    def page_click_detail(self):
        self.base_js(page.page_detail)

    # 点击详情中的开发联系单
    def page_click_developsheet(self):
        self.base_click(page.page_click_developsheet)

    # 输入试验名称
    def page_input_experiment_name(self,value):
        self.base_input(page.page_experiment_name,value)

    # 点击物料类别
    def page_click_material_calssify(self):
        self.base_click(page.page_material_classify)

    # 选择物料类别中的某一类
    def page_select_material_classify(self):
        self.base_click(page.page_select_material_classify)

    # 点击接收部门
    def page_click_accept_dept(self):
        self.base_click(page.page_accept_dept)

    # 选择接收部门中的某一部门
    def page_select_accept_dept(self):
        self.base_click(page.page_select_accept_dept)

    # 点击接收人
    def page_click_accept_people(self):
        self.base_click(page.page_accept_people)

    # 选择接收人中的某一人
    def page_select_accept_people(self):
        self.base_click(page.page_select_accept_people)

    # 输入试验目的
    def page_input_experiment_goal(self,goal_value):
        self.base_input(page.page_experiment_goal,goal_value)

    # 输入试验内容
    def page_input_experiment_content(self,content):
        self.base_input(page.page_experiment_content,content)

    # 输入试验要求与试验时间
    def page_input_experiment_order(self,order):
        self.base_input(page.page_experiment_order,order)

    #  点击提交审核
    def page_click_submit(self):
        self.base_click(page.page_click_submit)

    # 断言
    def page_is_if_supplier_developsheet_success(self):
        return self.base_if_is_exist(page.page_success_button)

    # 组合业务：填写开发联系单，并提交
    def page_supplier_qualificationdevelopsheet_submit(self,name,value,goal_value,content,order):
        self.page_search_supplier_developsheet(name)
        time.sleep(2)
        self.page_click_detail()
        time.sleep(2)
        self.page_click_developsheet()
        time.sleep(2)
        self.page_input_experiment_name(value)
        time.sleep(1)
        self.page_click_material_calssify()
        time.sleep(1)
        self.page_select_material_classify()
        time.sleep(1)
        self.page_click_accept_dept()
        time.sleep(1)
        self.page_select_accept_dept()
        time.sleep(1)
        self.page_click_accept_people()
        time.sleep(1)
        self.page_select_accept_people()
        time.sleep(1)
        self.page_input_experiment_goal(goal_value)
        time.sleep(1)
        self.page_input_experiment_content(content)
        time.sleep(1)
        self.page_input_experiment_order(order)
        time.sleep(1)
        self.page_click_submit()





