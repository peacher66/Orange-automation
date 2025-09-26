from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""

    # 元素定位器
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")
    LOGIN_TITLE = (By.CLASS_NAME, "orangehrm-login-title")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_login(self):
        """导航到登录页面"""
        self.driver.get(f"{self.base_url}/web/index.php/auth/login")
        return self

    def login(self, username, password):
        """
        执行登录操作

        Args:
            username: 用户名
            password: 密码

        Returns:
            bool: 登录是否成功
        """
        try:
            # 导航到登录页面
            self.navigate_to_login()

            # 等待元素加载
            self.wait_for_element(self.USERNAME_INPUT)

            # 输入用户名和密码
            self.input_text(self.USERNAME_INPUT, username)
            self.input_text(self.PASSWORD_INPUT, password)

            # 点击登录按钮
            self.click_element(self.LOGIN_BUTTON)

            # 等待登录完成
            self.wait.until(EC.url_contains("dashboard"))

            return True

        except Exception as e:
            print(f"登录失败: {e}")
            return False

    def get_error_message(self):
        """获取错误消息"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return ""

    def is_login_page_loaded(self):
        """检查登录页面是否加载完成"""
        return self.is_element_present(self.LOGIN_TITLE)