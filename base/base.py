import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from tool.logger import GetLogger

log = GetLogger().get_logger()

class Base:
    def __init__(self,driver):
        log.info('正在初始化获取driver对象：{}'.format(driver))
        self.driver = driver

    # 定位元素
    def base_find_element(self,loc,timeout = 30):
        log.info("正在查找元素：{}元素，最多等待：{}秒".format(loc,timeout))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=0.5).until(lambda x:x.find_element(*loc))

    # 点击操作
    def base_click(self,loc):
        log.info('正在点击:{}元素'.format(loc))
        self.base_find_element(loc).click()

    # 输入内容
    def base_input(self,loc,value):
        log.info('正在输入：{}元素 输入值是: {}'.format(loc, value))
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本内容
    def base_get_text(self,loc):
        log.info("定位到{}元素".format(loc))
        return self.base_find_element(loc).text

    # 添加cookie
    def base_add_cookie(self,name,value):
        log.info('正在添加cookie=====')
        self.driver.add_cookie({"name":name,"value":value})

    # 判断元素是否存在
    def base_if_is_exist(self,loc):
        try:
            log.info("判断{}元素是否存在".format(loc))
            self.base_find_element(loc)
            log.info("{}元素是存在的".format(loc))
            return True
        except:
            log.error("{}元素是不存在的".format(loc))
            return False

    # 模拟鼠标移动到某个元素上
    def base_move_to_cationchains(self,loc):
        action = ActionChains(self.driver)
        action.move_to_element(self.base_find_element(loc)).perform()
        time.sleep(2)
        action.release()

    # 编写js脚本
    def base_js(self, loc):
        log.info("定位{}元素成功，并且成功执行js".format(loc))
        self.driver.execute_script('arguments[0].click();',self.base_find_element(loc))

    # 上传文件
    def base_upload_file(self,loc,filePath):
        self.base_find_element(loc).send_keys(filePath)

    # 截图
    def base_get_image(self):
        log.error("报错截图")
        self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y-%m-%d %H_%M-%S')))

    # 获取源码
    @property
    def base_page_source(self):
        log.info("获取源码")
        return self.driver.page_source

    # js脚本修改时间日期
    def base_update_time(self,js,loc,value):
        self.driver.execute_script(js)
        time.sleep(3)
        self.base_input(loc,value)

    # js脚本修改时间日期
    def base_js_update_select(self,js,loc,value):
        self.driver.execute_script(js)
        time.sleep(3)
        js_value = self.base_find_element(loc).value = value
        self.driver.execute_script(js_value)

    # 关闭浏览器
    def base_close_driver(self):
        self.driver.close()

    # 回到首页
    def base_click_index(self,loc):
        self.base_click(loc)
























