'''公共功能的配置信息'''
from selenium.webdriver.common.by import By

'''供应商管理列表的搜索查询'''
# 供应商名称
common_search_supplier_name = By.XPATH, '//input[@placeholder="请输入供应商/申请人"]'
# 查询按钮
common_select_button = By.XPATH, '//button[@type="button"]/span[text() = "查询"]'

'''我的审核模块的搜索查询'''
# 供应商名称
common_process_supplier_name = By.XPATH, '//input[@placeholder="请输入供应商"]'
# 查询按钮
common_process_select_button = By.XPATH, '//button[@type="button"]/span[text() = "查询"]'


