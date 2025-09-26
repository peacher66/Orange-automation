import pytest
import time
from src.utils.config import Config


class TestPIMModule:
    """PIM模块测试"""

    def test_pim_navigation(self, pim_page):
        """测试PIM导航"""
        # 验证PIM页面加载
        assert pim_page.is_pim_page_loaded(), "PIM页面应该加载成功"

        # 验证URL包含pim
        assert "pim" in pim_page.get_current_url().lower(), "URL应该包含pim"

    def test_add_employee(self, pim_page):
        """测试添加员工"""
        # 生成唯一的员工信息
        timestamp = str(int(time.time()))
        first_name = f"{Config.TEST_FIRST_NAME}{timestamp}"
        last_name = f"{Config.TEST_LAST_NAME}{timestamp}"
        employee_id = f"EMP{timestamp}"

        # 添加员工
        result = pim_page.add_employee(first_name, last_name, employee_id)

        # 验证添加成功
        assert result, "员工添加应该成功"

        # 验证成功消息
        success_message = pim_page.get_success_message()
        assert "success" in success_message.lower(), f"应该有成功消息，实际是: {success_message}"

    def test_search_employee(self, pim_page):
        """测试搜索员工"""
        # 搜索员工
        pim_page.search_employee(Config.TEST_FIRST_NAME)

        # 这里可以添加搜索结果的验证
        # 例如检查搜索结果表格是否显示

    @pytest.mark.parametrize("first_name,last_name", [
        ("John", "Doe"),
        ("Jane", "Smith"),
        ("", "Lastname"),  # 空名字测试
    ])
    def test_add_employee_with_data(self, pim_page, first_name, last_name):
        """使用参数化测试添加员工"""
        if first_name and last_name:  # 只有有效数据才执行添加
            result = pim_page.add_employee(first_name, last_name)
            assert result, f"添加员工 {first_name} {last_name} 应该成功"