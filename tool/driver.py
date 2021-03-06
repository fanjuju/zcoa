from tool.openDriver import OpenDriver
import page

class GetDriver:

    # 获取浏览器，若没有，则打开
    driver = None
    @classmethod
    def get_driver(cls,url):
        if cls.driver is None:
            cls.driver = OpenDriver().get_driver(browser='chrome')
            cls.driver.get(url = url)
            cls.driver.maximize_window()
            return cls.driver

    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


