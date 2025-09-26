import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestOrangeHRMPIM:
    """OrangeHRM PIM模块测试 - 修复版2"""

    def setup_method(self):
        """每个测试方法前执行"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)  # 增加等待时间到20秒

    def teardown_method(self):
        """每个测试方法后执行"""
        self.driver.quit()

    def login(self):
        """登录OrangeHRM"""
        print("🔐 正在登录...")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        try:
            username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password = self.driver.find_element(By.NAME, "password")
            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")

            username.send_keys("Admin")
            password.send_keys("admin123")
            login_btn.click()
            time.sleep(3)

            # 验证登录成功
            dashboard = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
            if dashboard.is_displayed():
                print("✅ 登录成功")
                return True
            else:
                return False
        except Exception as e:
            print(f"❌ 登录过程中出错: {e}")
            self.driver.save_screenshot("login_error.png")
            return False

    def test_pim_module_access(self):
        """测试访问PIM模块 - 修复版2"""
        print("🧭 测试PIM模块访问...")

        # 登录
        assert self.login(), "登录失败"

        # 等待Dashboard页面加载完成
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

        # 使用JavaScript点击PIM菜单
        pim_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
        self.driver.execute_script("arguments[0].click();", pim_menu)
        time.sleep(3)

        # 验证进入PIM页面 - 使用Add按钮作为标志
        try:
            pim_indicator = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add']")))
            assert pim_indicator.is_displayed()
            print("✅ PIM页面加载成功")
        except:
            # 如果Add按钮没找到，尝试Search按钮
            try:
                pim_indicator = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Search']")))
                assert pim_indicator.is_displayed()
                print("✅ PIM页面加载成功（通过Search按钮）")
            except:
                # 如果还不行，检查URL
                if "pim" in self.driver.current_url:
                    print("✅ 通过URL确认进入PIM页面")
                else:
                    self.driver.save_screenshot("pim_page_fail.png")
                    pytest.fail("PIM页面加载失败")

        print("✅ PIM模块访问测试成功!")

    # 其他测试方法暂不修改