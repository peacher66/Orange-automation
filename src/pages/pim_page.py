from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage


class PIMPage(BasePage):
    """PIM页面"""

    # 元素定位器
    PIM_HEADER = (By.XPATH, "//h6[contains(text(),'PIM')]")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    EMPLOYEE_LIST_BUTTON = (By.XPATH, "//a[text()='Employee List']")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "oxd-text--toast-title")
    SEARCH_EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)

    def is_pim_page_loaded(self):
        """检查PIM页面是否加载完成"""
        return self.is_element_present(self.PIM_HEADER)

    def click_employee_list(self):
        """点击员工列表"""
        self.click_element(self.EMPLOYEE_LIST_BUTTON)
        return self

    def click_add_employee(self):
        """点击添加员工按钮"""
        self.click_element(self.ADD_BUTTON)
        return self

    def add_employee(self, first_name, last_name, employee_id=None):
        """
        添加新员工

        Args:
            first_name: 名字
            last_name: 姓氏
            employee_id: 员工ID（可选）

        Returns:
            bool: 添加是否成功
        """
        try:
            # 点击添加员工
            self.click_add_employee()

            # 等待添加员工页面加载
            self.wait_for_element(self.FIRST_NAME_INPUT)

            # 填写员工信息
            self.input_text(self.FIRST_NAME_INPUT, first_name)
            self.input_text(self.LAST_NAME_INPUT, last_name)

            if employee_id:
                self.input_text(self.EMPLOYEE_ID_INPUT, employee_id)

            # 点击保存
            self.click_element(self.SAVE_BUTTON)

            # 等待保存完成
            self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))

            return True

        except Exception as e:
            print(f"添加员工失败: {e}")
            return False

    def search_employee(self, employee_name):
        """搜索员工"""
        self.input_text(self.SEARCH_EMPLOYEE_NAME, employee_name)
        self.click_element(self.SEARCH_BUTTON)
        return self

    def get_success_message(self):
        """获取成功消息"""
        try:
            return self.get_text(self.SUCCESS_MESSAGE)
        except:
            return ""