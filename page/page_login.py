from base.base import Base


class PageLogin(Base):

    # 用cookie进行登录
    def page_login(self,name,value):
        self.base_add_cookie(name,value)

    # 登录成功
    def page_login_success(self):
        self.page_login("ZCSESSIONID","2edd7db5-43b2-43c9-be9c-b26a16bffd1e")

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('http://test.buy.zcabc.com')
    login = PageLogin(driver).page_login_success()