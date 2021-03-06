from base.base import Base
import common

class SearchProcess(Base):
    # 输入供应商名称
    def common_process_supplier_name(self,name):
        self.base_input(common.common_process_supplier_name,name)

    # 点击查询
    def common_process_select_button(self):
        self.base_click(common.common_process_select_button)
