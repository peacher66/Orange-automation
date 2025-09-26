import os


class Config:
    """配置类"""

    # OrangeHRM 测试环境配置
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    PIM_URL = f"{BASE_URL}/pim/viewEmployeeList"

    # 测试账号
    ADMIN_USERNAME = "Admin"
    ADMIN_PASSWORD = "admin123"

    # 浏览器配置
    BROWSER = "chrome"  # chrome, firefox, edge
    HEADLESS = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 10

    # 测试数据
    TEST_FIRST_NAME = "Test"
    TEST_LAST_NAME = "User"
    TEST_EMPLOYEE_ID = "1001"

    # 报告配置
    REPORT_DIR = "reports"
    SCREENSHOT_DIR = "screenshots"

    @classmethod
    def setup_directories(cls):
        """创建必要的目录"""
        for directory in [cls.REPORT_DIR, cls.SCREENSHOT_DIR]:
            if not os.path.exists(directory):
                os.makedirs(directory)