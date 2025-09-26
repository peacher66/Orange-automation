import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class Config:
    """配置类"""

    # 应用配置
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")

    # 用户配置
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

    # 浏览器配置
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

    # 路径配置
    SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "reports/screenshots")
    REPORT_DIR = os.getenv("REPORT_DIR", "reports")

    # 测试数据
    TEST_FIRST_NAME = "Test"
    TEST_LAST_NAME = "User"

    @classmethod
    def setup_directories(cls):
        """创建必要的目录"""
        os.makedirs(cls.SCREENSHOT_DIR, exist_ok=True)
        os.makedirs(cls.REPORT_DIR, exist_ok=True)