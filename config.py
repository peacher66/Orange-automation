class Config:
    """测试配置类"""

    # 应用配置
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"
    PIM_URL = f"{BASE_URL}/web/index.php/pim/viewEmployeeList"

    # 测试账号
    USERNAME = "Admin"
    PASSWORD = "admin123"

    # 浏览器配置
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15

    # 测试数据
    TEST_FIRST_NAME = "Test"
    TEST_LAST_NAME_PREFIX = "User"

    # 路径配置
    REPORT_DIR = "reports"
    SCREENSHOT_DIR = "screenshots"

    @classmethod
    def get_unique_employee_name(cls):
        """生成唯一的员工姓名"""
        import time
        timestamp = int(time.time())
        return f"{cls.TEST_FIRST_NAME}", f"{cls.TEST_LAST_NAME_PREFIX}{timestamp}"


