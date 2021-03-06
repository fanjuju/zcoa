from selenium import webdriver

class OpenDriver:

    def driver(self,browser = 'chrome'):
        self.get_driver(browser=browser)

    def get_driver(self,browser):
        if browser == '360':
            return webdriver.Ie()
        elif browser == 'chrome':
            return webdriver.Chrome()
        elif browser == 'fixefox':
            return webdriver.Firefox()