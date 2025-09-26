from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utils.config import Config
import time



class BasePage:
    """页面对象基类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.base_url = Config.BASE_URL

    def is_element_present(self, locator):
        """检查元素是否存在"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def wait_for_element(self, locator, timeout=None):
        """等待元素出现"""
        if timeout is None:
            timeout = Config.EXPLICIT_WAIT

        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def click_element(self, locator, timeout=None):
        """点击元素"""
        element = self.wait_for_element(locator, timeout)
        if element:
            element.click()
            return True
        return False

    def input_text(self, locator, text, timeout=None):
        """输入文本"""
        element = self.wait_for_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def get_text(self, locator, timeout=None):
        """获取元素文本"""
        element = self.wait_for_element(locator, timeout)
        if element:
            return element.text
        return ""

    def take_screenshot(self, name):
        """截取屏幕截图"""
        Config.setup_directories()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{Config.SCREENSHOT_DIR}/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename

    def get_current_url(self):
        """获取当前URL"""
        return self.driver.current_url