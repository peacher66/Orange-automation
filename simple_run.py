# simple_run.py
import subprocess
import sys
import os


def run_tests():
    """运行测试的简单版本"""

    # 检查测试文件是否存在
    test_files = [
        "tests/test_pim.py",
        "test_pim.py",
        "tests.py"
    ]

    test_file = None
    for file in test_files:
        if os.path.exists(file):
            test_file = file
            break

    if not test_file:
        print("❌ 没有找到测试文件，正在创建简单的测试文件...")
        create_simple_test()
        test_file = "simple_test.py"

    # 运行pytest
    cmd = [sys.executable, "-m", "pytest", test_file, "-v", "--html=reports/report.html"]

    try:
        result = subprocess.run(cmd, check=True)
        print("🎉 测试完成!")
    except subprocess.CalledProcessError as e:
        print(f"❌ 测试失败: {e}")
        return e.returncode

    return 0


def create_simple_test():
    """创建简单的测试文件"""
    test_content = '''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSimpleOrangeHRM:
    """简单的OrangeHRM测试"""

    def test_login(self):
        """测试登录功能"""
        driver = webdriver.Chrome()
        driver.maximize_window()

        try:
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

            # 等待页面加载
            wait = WebDriverWait(driver, 10)

            # 输入凭据
            username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password = driver.find_element(By.NAME, "password")
            login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

            username.send_keys("Admin")
            password.send_keys("admin123")
            login_btn.click()

            # 验证登录成功
            dashboard = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
            assert dashboard.is_displayed()
            print("✅ 登录测试成功!")

        finally:
            driver.quit()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

    with open("simple_test.py", "w", encoding="utf-8") as f:
        f.write(test_content)
    print("📄 已创建简单测试文件: simple_test.py")


if __name__ == "__main__":
    sys.exit(run_tests())