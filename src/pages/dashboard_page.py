from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class DashboardPage(BasePage):
    """OrangeHRM仪表盘页面"""

    # 页面元素定位器
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_displayed(self):
        """检查仪表盘是否显示"""
        return self.is_element_present(self.DASHBOARD_HEADER)

    def click_pim_menu(self):
        """点击PIM菜单"""
        self.click_element(self.PIM_MENU)
        return self

    def logout(self):
        """执行登出操作"""
        self.click_element(self.USER_DROPDOWN)
        self.click_element(self.LOGOUT_LINK)
        return self

    def get_dashboard_header(self):
        """获取仪表盘标题"""
        return self.get_text(self.DASHBOARD_HEADER)