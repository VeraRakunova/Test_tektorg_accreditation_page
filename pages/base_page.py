from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
