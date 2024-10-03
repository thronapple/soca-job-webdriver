from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.config import Config

class WebDriverManager:
    def __init__(self):
        self.drivers = {}
    
    def create_driver(self, browser_type='chrome'):
        if len(self.drivers) >= Config.MAX_INSTANCES:
            return None, '达到最大实例数限制'
        
        if browser_type == 'chrome':
            options = ChromeOptions()
            if Config.BROWSER_OPTIONS['chrome']['headless']:
                options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
        elif browser_type == 'firefox':
            options = FirefoxOptions()
            if Config.BROWSER_OPTIONS['firefox']['headless']:
                options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        else:
            return None, '不支持的浏览器类型'

        driver_id = id(driver)
        self.drivers[driver_id] = driver
        return driver_id, None
    
    def get_driver(self, driver_id):
        return self.drivers.get(driver_id)
    
    def close_driver(self, driver_id):
        driver = self.drivers.pop(driver_id, None)
        if driver:
            driver.quit()
