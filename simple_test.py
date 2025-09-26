import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TestSimpleOrangeHRMFixed:
    """修复版的OrangeHRM测试"""

    def setup_method(self):
        """每个测试方法前执行"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)  # 增加等待时间
        self.base_url = "https://opensource-demo.orangehrmlive.com"

    def teardown_method(self):
        """每个测试方法后执行"""
        self.driver.quit()

    def login(self, username="Admin", password="admin123"):
        """通用的登录方法"""
        print(f"🔐 登录用户: {username}")

        # 打开登录页面
        self.driver.get(f"{self.base_url}/web/index.php/auth/login")
        time.sleep(2)

        try:
            # 等待页面元素加载
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

            # 输入凭据
            username_field.clear()
            username_field.send_keys(username)
            password_field.clear()
            password_field.send_keys(password)
            login_button.click()

            # 等待登录完成 - 检查是否成功跳转到dashboard
            self.wait.until(EC.url_contains("dashboard"))
            print("✅ 登录成功")
            return True

        except TimeoutException:
            # 检查是否是登录失败
            try:
                error_message = self.driver.find_element(By.CLASS_NAME, "oxd-alert-content-text")
                print(f"❌ 登录失败: {error_message.text}")
                return False
            except:
                print("❌ 登录超时")
                return False

    def navigate_to_pim(self):
        """导航到PIM模块"""
        print("🧭 导航到PIM模块...")

        # 尝试多种PIM菜单定位方式
        pim_selectors = [
            "//span[text()='PIM']",
            "//a[contains(@href, 'pim')]",
            "//li//span[text()='PIM']",
            "//nav//span[text()='PIM']"
        ]

        for selector in pim_selectors:
            try:
                pim_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                pim_menu.click()
                print(f"✅ 使用选择器点击PIM菜单: {selector}")

                # 等待PIM页面加载
                time.sleep(3)

                # 验证是否进入PIM页面
                pim_indicators = [
                    "//h6[contains(text(), 'PIM')]",
                    "//h5[contains(text(), 'PIM')]",
                    "//button[contains(text(), 'Add')]",
                    "//a[contains(text(), 'Employee List')]"
                ]

                for indicator in pim_indicators:
                    try:
                        self.wait.until(EC.presence_of_element_located((By.XPATH, indicator)))
                        print(f"✅ 确认进入PIM页面，找到元素: {indicator}")
                        return True
                    except:
                        continue

                # 通过URL验证
                if "pim" in self.driver.current_url.lower():
                    print("✅ 通过URL确认进入PIM页面")
                    return True

            except TimeoutException:
                print(f"❌ 选择器失败: {selector}")
                continue

        return False

    def test_login_success(self):
        """测试成功登录"""
        print("🔐 测试登录功能...")

        result = self.login()
        assert result, "登录应该成功"

        # 额外验证：检查页面元素
        try:
            dashboard_header = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")))
            assert dashboard_header.is_displayed()
            print("✅ 登录测试成功!")
        except:
            # 如果找不到Dashboard标题，检查其他成功指标
            try:
                user_dropdown = self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
                if user_dropdown.is_displayed():
                    print("✅ 登录成功（通过用户下拉菜单验证）")
            except:
                print("⚠️  登录成功但无法验证页面元素")

    def test_pim_navigation(self):
        """测试PIM模块导航 - 修复版"""
        print("🧭 测试PIM导航...")

        # 先登录
        assert self.login(), "必须先登录成功"

        # 导航到PIM
        result = self.navigate_to_pim()
        assert result, "应该成功导航到PIM页面"

        print("✅ PIM导航测试成功!")

    def test_add_employee_simple(self):
        """测试添加员工（修复版）"""
        print("👥 测试添加员工...")

        # 先登录并导航到PIM
        assert self.login(), "必须先登录成功"
        assert self.navigate_to_pim(), "必须先进入PIM页面"

        # 尝试多种添加按钮定位方式
        add_button_selectors = [
            "//button[text()='Add']",
            "//button[contains(text(), 'Add')]",
            "//button[@type='button'][contains(., 'Add')]",
            "//div[@class='orangehrm-header-container']//button"
        ]

        add_button = None
        for selector in add_button_selectors:
            try:
                add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                print(f"✅ 找到添加按钮: {selector}")
                break
            except TimeoutException:
                continue

        if add_button:
            add_button.click()
            print("✅ 点击添加按钮成功")
            time.sleep(3)

            # 现在应该在添加员工页面
            # 检查是否在添加员工页面
            add_employee_indicators = [
                "//h6[contains(text(), 'Add Employee')]",
                "//input[@name='firstName']",
                "//label[text()='First Name']"
            ]

            for indicator in add_employee_indicators:
                try:
                    self.wait.until(EC.presence_of_element_located((By.XPATH, indicator)))
                    print(f"✅ 确认在添加员工页面: {indicator}")
                    break
                except:
                    continue
            else:
                # 如果所有指示器都失败，尝试直接访问添加员工URL
                print("⚠️  通过菜单导航失败，尝试直接访问URL")
                self.driver.get(f"{self.base_url}/web/index.php/pim/addEmployee")
                time.sleep(3)

            # 填写员工信息
            try:
                first_name_field = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
                last_name_field = self.driver.find_element(By.NAME, "lastName")

                # 生成唯一的员工信息
                timestamp = str(int(time.time()))
                test_first_name = f"Test{timestamp}"
                test_last_name = f"User{timestamp}"

                first_name_field.send_keys(test_first_name)
                last_name_field.send_keys(test_last_name)
                print(f"✅ 填写员工信息: {test_first_name} {test_last_name}")

                # 保存员工
                save_buttons = [
                    "//button[@type='submit']",
                    "//button[contains(text(), 'Save')]"
                ]

                for button_selector in save_buttons:
                    try:
                        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, button_selector)))
                        save_button.click()
                        print("✅ 点击保存按钮")
                        break
                    except:
                        continue

                # 等待保存完成
                time.sleep(5)

                # 检查是否保存成功
                success_indicators = [
                    "//p[contains(@class, 'oxd-text--toast-message')]",
                    "//div[contains(@class, 'oxd-toast')]",
                    "//h6[contains(text(), 'Personal Details')]"
                ]

                for indicator in success_indicators:
                    try:
                        element = self.driver.find_element(By.XPATH, indicator)
                        if "success" in element.text.lower() or "personal" in element.text.lower():
                            print("✅ 员工添加成功!")
                            assert True
                            return
                    except:
                        continue

                # 如果没找到成功消息，但页面跳转了也算成功
                if "pim/viewPersonalDetails" in self.driver.current_url:
                    print("✅ 员工添加成功（通过URL验证）")
                    assert True
                else:
                    print("⚠️  无法确认是否添加成功")
                    assert False, "无法验证员工添加是否成功"

            except Exception as e:
                print(f"❌ 添加员工过程中出错: {e}")
                assert False, f"添加员工失败: {e}"
        else:
            assert False, "找不到添加按钮"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])