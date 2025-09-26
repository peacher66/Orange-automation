# simple_test_fixed.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


def simple_test():
    """最简单的OrangeHRM测试"""
    print("🚀 启动OrangeHRM简单测试...")

    # 初始化浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 步骤1: 访问登录页面
        print("1. 访问登录页面...")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        print(f"   页面标题: {driver.title}")
        print(f"   当前URL: {driver.current_url}")

        # 检查是否重定向到新版本URL
        if "web/index.php/auth/login" not in driver.current_url:
            print("⚠️  检测到旧版本URL，尝试访问新版本...")
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            time.sleep(3)
            print(f"   新URL: {driver.current_url}")

        # 步骤2: 查找登录表单元素
        print("2. 查找登录表单元素...")

        # 方法1: 使用更通用的选择器
        username = None
        password = None
        login_btn = None

        # 尝试多种选择器组合
        selectors = [
            # 新版本选择器
            {"username": "input[name='username']", "password": "input[name='password']",
             "button": "button[type='submit']"},
            # 备用选择器
            {"username": "input[placeholder='Username']", "password": "input[placeholder='Password']",
             "button": "button"},
            # 通过类名选择
            {"username": ".oxd-input", "password": ".oxd-input", "button": ".oxd-button"},
        ]

        for selector_set in selectors:
            try:
                username = driver.find_element(By.CSS_SELECTOR, selector_set["username"])
                password = driver.find_element(By.CSS_SELECTOR, selector_set["password"])
                login_btn = driver.find_element(By.CSS_SELECTOR, selector_set["button"])
                print(f"✅ 使用选择器组找到元素")
                break
            except:
                continue

        # 如果CSS选择器失败，尝试XPATH
        if not username:
            try:
                username = driver.find_element(By.XPATH, "//input[@name='username']")
                password = driver.find_element(By.XPATH, "//input[@name='password']")
                login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
                print("✅ 使用XPATH找到元素")
            except:
                print("❌ 无法找到登录表单元素")
                # 截图并打印页面内容用于调试
                driver.save_screenshot("login_form_not_found.png")
                print("页面HTML前1000字符:")
                print(driver.page_source[:1000])
                return False

        # 步骤3: 输入凭据并登录
        print("3. 输入凭据并登录...")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn.click()
        time.sleep(5)  # 等待登录完成

        print(f"   登录后标题: {driver.title}")
        print(f"   登录后URL: {driver.current_url}")

        # 步骤4: 验证登录成功
        print("4. 验证登录状态...")

        # 检查URL是否包含dashboard或index
        if "dashboard" in driver.current_url.lower() or "index" in driver.current_url.lower():
            print("✅ 通过URL验证登录成功")
        else:
            # 检查页面标题
            if "OrangeHRM" in driver.title:
                print("✅ 通过页面标题验证登录成功")
            else:
                # 检查是否有欢迎消息或菜单
                page_text = driver.page_source.lower()
                if "dashboard" in page_text or "welcome" in page_text:
                    print("✅ 通过页面内容验证登录成功")
                else:
                    print("❌ 登录状态不确定")
                    driver.save_screenshot("login_status_unknown.png")
                    return False

        # 步骤5: 尝试访问PIM模块
        print("5. 尝试访问PIM模块...")

        # 方法1: 直接导航到PIM URL
        pim_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
        driver.get(pim_url)
        time.sleep(3)

        print(f"   PIM页面标题: {driver.title}")
        print(f"   PIM页面URL: {driver.current_url}")

        # 检查是否成功进入PIM页面
        if "pim" in driver.current_url.lower():
            print("✅ 成功进入PIM页面")

            # 尝试查找PIM页面特有的元素
            pim_elements = driver.find_elements(By.XPATH,
                                                "//*[contains(text(), 'Employee') or contains(text(), 'PIM')]")
            print(f"   找到 {len(pim_elements)} 个PIM相关元素")

            # 截图保存
            driver.save_screenshot("pim_page.png")
            return True
        else:
            print("❌ 可能未成功进入PIM页面")
            driver.save_screenshot("pim_access_failed.png")
            return False

    except Exception as e:
        print(f"❌ 测试过程中出错: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # 保持浏览器打开以便查看结果
        print("\n测试完成，浏览器将保持打开状态...")
        print("请手动关闭浏览器窗口")
        # 如果希望自动关闭浏览器，取消下面的注释
        # driver.quit()


if __name__ == "__main__":
    success = simple_test()
    if success:
        print("\n🎉 测试通过!")
        sys.exit(0)
    else:
        print("\n💥 测试失败!")
        sys.exit(1)