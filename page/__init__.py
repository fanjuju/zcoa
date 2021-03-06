'''配置信息'''

from selenium.webdriver.common.by import By

url_2090 = 'http://test.buy.zcabc.com/#/homepage?userId=2090'
url_204 = 'http://test.buy.zcabc.com/#/homepage?userId=204'
index_url = "http://test.buy.zcabc.com/#/supplierManage/suppliesInto/list"

'''供应商引入新增流程配置信息'''

# 供应商管理tap栏
page_click_supplier = By.XPATH, '//span[@slot="title" and text() = "供应商管理"]'
# 供应商引入选择项
page_select_suppier_apply = By.XPATH, '//ul[@role="menu"]/li[text() = " 供应商引入 "]'
# 新增按钮
page_add_button = By.XPATH, '//button[@type="button"]/span[text()="新增"]'
# 引入原料选项框
page_click_applier_apply = By.XPATH, '//input[@placeholder="请选择引入原料"]'
# 引入原料下拉选择
page_select_material_name = By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[7]'
# 下拉选项
page_js_select_material_name = By.XPATH, "document.querySelector('.el-input__inner').removeAttribute('readonly')"
# 供应商
page_input_supplier_name = By.XPATH, '//input[@placeholder="请输入供应商"]'
# 具体情况描述
page_input_remark = By.XPATH, '(//textarea[@class="el-textarea__inner"])[1]'
# 建议
page_input_suggest = By.XPATH, '(//textarea[@class="el-textarea__inner"])[2]'
# 点击提交
page_click_submit_button = By.XPATH, '//button/span[text() = "提交审核"]'
# 继续提交
page_contine_submit_button = By.XPATH, '//div[@class="dialog-footer"]/button/span[text() = "继续提交"]'
# 操作成功提示
page_success_button = By.XPATH, '//p[text() = "操作成功"]'
# 定位首页列表
page_index_list = By.XPATH, '//span[text() = " 列表 "]'

'''供方开拓审核配置信息'''

# 我的审核tap栏
page_click_my_process = By.XPATH, '//span[@slot="title" and text() = "我的审核"]'
# 供方开拓审核按钮
page_click_supplier_development = By.XPATH, '//dt[@class="fl name" and text() = "供方开拓审核"]'
# 待办理列表
page_task_list = By.XPATH, '//div[text() = "待办理"]'
# 操作栏的办理按钮
page_select_pending_supplier = By.XPATH, '(//span[@class="click-active ripple" and text() = "办理"])[1]'
# 移动到办理按钮后
page_select_pending_supplier_after = By.XPATH, '(//tr[@class="el-table__row hover-row"]/td/div/div/span[text() = "办理"])[1]'
# 鼠标移动到查询按钮，目的是为了消除类别的弹出窗
page_select_button = By.XPATH, '//button[@type="button" ]/span[text() = "查询"]'
# 审核详情页中的办理按钮
page_click_apply = By.XPATH, '//button[@type="button"]/span[text() = "办理"]'
# 办理弹窗中的审核意见，同意按钮
page_select_process_pass = By.XPATH, '(//label[@role="radio"]/span/span)[1]'
# 审核说明栏
page_input_process_remark = By.XPATH, '//textarea[@placeholder="请输入..."]'
# 确定按钮
page_click_confirm = By.XPATH, '//span[text()="确 定"]'
# todo 提交后是否有成功处理的提示语
page_process_success = By.XPATH, '//p[text()="成功处理：1，失败：0"]'

'''供应商资质的配置信息'''
# 列表详情按钮
page_detail = By.XPATH, '(//span[@class and text() = "详情"])[2]'
# 供应商资质tap栏中的资质信息明细
# page_qualification_details = By.XPATH, '(//span[text() = "上传附件"])[1]'
page_qualification_details = By.XPATH, '(//input[@type="file" and @name="file"])[1]'
# 资质评估报告
# page_qualification_report = By.XPATH, '(//span[text() = "上传附件"])[2]'
page_qualification_report = By.XPATH, '(//input[@type="file" and @name="file"])[2]'
# 提交审核
page_click_submit = By.XPATH, '//span[text() = "提交审核"]'

'''供应商资质审核'''
# 供应商资质审核
page_qualification_process = By.XPATH, '//dt[text() = "资质审核"]'
# 审核列表中的办理按钮
page_qualification_apply = By.XPATH, '(//span[@class="click-active ripple" and text() = "办理"])[1]'

'''开发联系单的配置信息'''
# 详情页中点击开发联系单
page_click_developsheet = By.XPATH, '//div[@id="tab-2" and text()="开发联系单"]'
# 试验名称
page_experiment_name = By.XPATH, '//input[@placeholder="请填写试验名称"]'
# 类别
page_material_classify = By.XPATH, '//input[@placeholder="请选择类别"]'
# 类别中的某一项
page_select_material_classify = By.XPATH, '((//div[@class = "el-scrollbar"])[3]/descendant::*/li)[2]'
# 接收部门
page_accept_dept = By.XPATH, '//input[@placeholder="请选择接收部门"]'
# 接收部门中的某一个部门
page_select_accept_dept = By.XPATH, '(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/li/span[text() = "柯桥基地"]'
# 接收人
page_accept_people = By.XPATH, '//input[@placeholder="请选择接收人"]'
# 接收人中的某一个人
page_select_accept_people = By.XPATH, '((//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]/child::*)[2]'
# 试验目的
page_experiment_goal = By.XPATH, '//textarea[@placeholder="请填写试验目的"]'
# 试验内容
page_experiment_content = By.XPATH, '//textarea[@placeholder="请填写试验内容"]'
# 试验要求与试验时间
page_experiment_order = By.XPATH, '//textarea[@placeholder="试验要求与试验时间"]'


'''开发联系单审核'''
# 开发联系单审核按钮
page_developsheet_process = By.XPATH, '//dt[@class="fl name" and text() = "开发联系单审核"]'


'''试方试料的配置信息'''
# 试方试料按钮
page_materialtest = By.XPATH, '//div[text()="试方试料"]'
# 批试的地址
page_material_finish = By.XPATH, '(//div[@class="el-checkbox-group"]/child::*)[3]'
# 评审意见
page_idea = By.XPATH, '//textarea[@placeholder="请填写评审意见"]'
# 材料报告
page_material_report = By.XPATH, '//input[@name="file"]'


'''试方试料审核'''
# 试方试料审核按钮
page_materialtest_button = By.XPATH, '//dt[@class="fl name" and text() = "试方试料审核"]'


'''现场考察的配置信息'''
# 现场考察tap栏
page_insepct = By.XPATH, '//div[text()="现场考察"]'
# 现场考察人员
page_insepct_name = By.XPATH, '//input[@placeholder="请填写考察人员"]'
# 考察性质
page_insepct_property = By.XPATH, '//input[@placeholder="请选择考察性质"]'
# 考察性质选择定期考察
page_insepct_property_value = By.XPATH, '((//div[@class = "el-scrollbar"])/div/ul/li)[2]'
# 考察开始时间
page_insepct_starttime = By.XPATH, '//input[@placeholder="请选择考察开始时间"]'
# 修改时间的js脚本
page_js = 'document.querySelector(".el-popper").style.display = "block"'
# 考察结束时间
page_insepct_endtime = By.XPATH, '//input[@placeholder="请选择考察结束时间"]'
# 考察地点
page_insepct_address = By.XPATH, '//input[@placeholder = "请选择考察地点"]'
# 考察地点-省
page_insepct_address_province = By.XPATH, '//span[text() = "广东省"]'
# 考察地点-市
page_insepct_address_city = By.XPATH, '//span[text() = "佛山市"]'
# 考察地点-区
page_insepct_address_area = By.XPATH, '//span[text() = "顺德区"]'
# 详细地址
page_insepct_detailed_address = By.XPATH, '//input[@placeholder = "请填写详细地址"]'

'''现场考察审核'''
# 现场考察审核按钮
page_insepct_button = By.XPATH, '//dt[text() = "现场考察审核"]'
# 纳入申请按钮
page_inapplication_button = By.XPATH, '(//span[text() = "纳入申请"])[2]'
# 确定弹窗中的确定按钮
page_inapplication_confirm = By.XPATH, '(//button[@type="button"])[12]/span'

'''纳入申请审核'''
# 纳入申请按钮
page_inapplication_process_button = By.XPATH, '//dt[text() = "纳入申请审核"]'




