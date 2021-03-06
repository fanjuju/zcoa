from base.base import Base
import time
import page

class SupplierApply(Base):
    # 点击供应商管理tap栏
    def page_click_supplier(self):
        self.base_click(page.page_click_supplier)

    # 选择供应商引入项
    def page_select_suppier_apply(self):
        self.base_click(page.page_select_suppier_apply)

    # 点击新增按钮
    def page_add_button(self):
        self.base_click(page.page_add_button)

    # 点击引入原料下拉框
    def page_click_applier_apply(self):
        self.base_click(page.page_click_applier_apply)

    # 下拉选择引入原料名称
    def page_select_material_name(self):
        self.base_click(page.page_select_material_name)

    # 输入供应商名称
    def page_input_supplier_name(self,name):
        self.base_input(page.page_input_supplier_name,name)


    # 具体情况描述信息添加
    def page_input_remark(self,note):
        self.base_input(page.page_input_remark,note)


    # 建议信息添加
    def page_input_suggest(self,suggest):
        self.base_input(page.page_input_suggest,suggest)


    # # 获取提示框中的文本内容
    # def page_get_text(self):
    #     self.base_get_text(loc)

    # 提交---不超过6家
    def page_click_submit_button(self):
        self.base_click(page.page_click_submit_button)

    # # 提交---超过6家
    # def page_more_six_submit_button(self):
    # 继续提交---超过6家
    def page_contine_submit_button(self):
        self.base_click(page.page_contine_submit_button)

    def page_submit(self):
        if self.driver.current_url == page.index_url:
            self.driver.close()
            # # time.sleep(5)
            # # self.base_click_index(page.page_index_list)
            # if :
            #     self.driver.quit()
            # else:
            #     print("提交报错")
        else:
            # time.sleep(2)
            self.page_contine_submit_button()

    # 断言
    def page_success_button_is_exist(self):
        return self.base_if_is_exist(page.page_success_button)



    # 组合业务
    def page_supplier_apply(self,name,note,suggest):
        self.page_click_supplier()
        time.sleep(2)
        self.page_select_suppier_apply()
        time.sleep(2)
        self.page_add_button()
        time.sleep(2)
        self.page_click_applier_apply()
        time.sleep(2)
        self.page_select_material_name()
        time.sleep(2)
        self.page_input_supplier_name(name)
        time.sleep(2)
        self.page_input_remark(note)
        time.sleep(2)
        self.page_input_suggest(suggest)
        time.sleep(2)
        self.page_click_submit_button()
        time.sleep(2)
        # self.page_submit()


