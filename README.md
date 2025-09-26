 OrangeHRM 自动化测试项目

<div align="center">

 🧪 OrangeHRM 自动化测试框架

专业级的人力资源管理系统自动化测试方案

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-43B02A?logo=selenium&logoColor=white)](https://selenium.dev)
[![Pytest](https://img.shields.io/badge/Pytest-7.4%2B-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/orangehrm-automation?style=social)](https://github.com/your-username/orangehrm-automation)

基于 Page Object Model 设计模式的现代化测试框架

</div>

 📖 目录

- [项目概述](-项目概述)
- [核心特性](-核心特性)
- [项目结构](-项目结构)
- [快速开始](-快速开始)
- [功能覆盖](-功能覆盖)
- [技术架构](-技术架构)
- [使用指南](-使用指南)
- [配置说明](-配置说明)
- [故障排除](-故障排除)
- [贡献指南](-贡献指南)
- [开发路线图](-开发路线图)
- [许可证](-许可证)

 🎯 项目概述

 项目简介
OrangeHRM 自动化测试项目是一个基于 Selenium WebDriver 和 Python 构建的完整测试框架，专门为 OrangeHRM 人力资源管理系统设计。本项目采用业界标准的 Page Object Model (POM) 设计模式，确保代码的可维护性、可读性和可扩展性。

 设计理念
- 模块化设计: 每个功能模块独立封装，便于维护和扩展
- 数据驱动测试: 支持参数化测试，提高测试覆盖率
- 智能等待机制: 自动处理页面加载和元素等待，提升测试稳定性
- 详细报告系统: 自动生成 HTML 测试报告和失败截图

 适用场景
- 🔍 回归测试: 确保新功能不影响现有业务
- 🚀 持续集成: 集成到 CI/CD 流水线中
- 📊 质量监控: 监控系统关键功能的稳定性
- 🧪 功能验证: 验证业务逻辑的正确性

 ✨ 核心特性

 架构优势
| 特性 | 描述 | 优势 |
|------|------|------|
| 🏗️ POM 设计模式 | 页面元素与测试逻辑分离 | 提高代码复用性和可维护性 |
| 📊 智能报告 | 自动生成 HTML 报告和截图 | 快速定位问题，便于团队协作 |
| ⚡ 高效执行 | 并行测试和智能等待机制 | 缩短测试执行时间 |
| 🔧 易于扩展 | 模块化架构和清晰接口 | 快速添加新测试用例 |

 技术特色
- 多浏览器支持: 支持 Chrome、Firefox、Edge 等主流浏览器
- 跨平台兼容: 支持 Windows、Linux、macOS 操作系统
- 灵活配置: 通过配置文件轻松切换测试环境
- 错误恢复: 自动重试机制和详细的错误日志

 📁 项目结构

```plaintext
orangehrm-automation/
├── 📂 src/                            源代码目录
│   ├── 📂 pages/                     页面对象模型 (POM)
│   │   ├── __init__.py
│   │   ├── 🔧 base_page.py           页面基类 - 封装通用方法
│   │   ├── 🔐 login_page.py          登录页面对象
│   │   ├── 📊 dashboard_page.py      仪表盘页面对象
│   │   └── 👥 pim_page.py            PIM 模块页面对象
│   └── 📂 utils/                     工具类目录
│       ├── __init__.py
│       └── ⚙️ config.py              配置文件管理
├── 📂 tests/                         测试用例目录
│   ├── __init__.py
│   ├── 🔧 conftest.py               Pytest 配置和 Fixture
│   ├── ✅ test_pim.py               PIM 模块单元测试
│   └── 🔄 complete_pim_test.py      完整 PIM 测试套件
├── 📂 reports/                       测试报告目录 (自动生成)
├── 📂 screenshots/                   截图目录 (自动生成)
├── 🚀 run_tests.py                  基础测试运行脚本
├── 🔥 run_comprehensive_test.py     全面测试运行脚本
├── 📋 requirements.txt              项目依赖列表
├── ⚙️ config.py                     项目配置文件
├── 📝 .gitignore                    Git 忽略文件配置
└── 📖 README.md                     项目说明文档
```

 🚀 快速开始

 环境要求

 系统要求
- 操作系统: Windows 10/11, macOS 10.14+, Ubuntu 16.04+
- Python: 3.8 或更高版本
- 内存: 最少 4GB RAM
- 磁盘空间: 最少 1GB 可用空间

 软件依赖
- Chrome 浏览器: 版本 90+
- Git: 版本控制工具

 安装步骤

 1. 克隆项目仓库
```bash
 克隆项目到本地
git clone https://github.com/your-username/orangehrm-automation.git

 进入项目目录
cd orangehrm-automation
```

 2. 创建虚拟环境
```bash
 创建虚拟环境
python -m venv venv

 激活虚拟环境
 Windows
venv\Scripts\activate
 Linux/macOS
source venv/bin/activate
```

 3. 安装项目依赖
```bash
 安装所有依赖包
pip install -r requirements.txt

 验证安装是否成功
python -c "import selenium; print('Selenium 安装成功')"
```

 4. 运行测试示例
```bash
 运行快速验证测试
python run_tests.py

 或运行完整测试套件
python run_comprehensive_test.py
```

 验证安装

安装完成后，可以通过以下命令验证环境配置是否正确：

```bash
 检查 Python 版本
python --version

 检查依赖包安装
pip list | grep -E "(selenium|pytest)"

 运行简单验证脚本
python -c "
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com')
print('浏览器驱动正常')
driver.quit()
"
```

 🧪 功能覆盖

 测试范围总览

| 模块 | 功能点 | 测试状态 | 优先级 |
|------|--------|----------|--------|
| 用户认证 | 登录/登出功能 | ✅ 已完成 | 🔴 高 |
| PIM 模块 | 员工信息管理 | ✅ 已完成 | 🔴 高 |
| 考勤管理 | 请假/考勤流程 | 🟡 计划中 | 🟡 中 |
| 薪资管理 | 薪资计算发放 | 🟡 计划中 | 🟡 中 |

 详细功能说明

 🔐 用户认证模块
- ✅ 登录功能测试
  - 有效凭据登录验证
  - 无效凭据错误处理
  - 登录状态持久化
  - 会话安全验证

- ✅ 权限验证
  - 角色基础权限检查
  - 页面访问权限控制
  - 功能模块权限验证

 👥 员工信息管理 (PIM) 模块
- ✅ 员工增删改查
  - 添加新员工（必填字段验证）
  - 员工信息编辑更新
  - 员工信息搜索筛选
  - 员工记录删除操作

- ✅ 数据验证
  - 表单字段验证规则
  - 数据完整性检查
  - 业务逻辑验证

 🔄 业务流程测试
- ✅ 端到端流程验证
  - 员工完整生命周期管理
  - 多步骤业务流程验证
  - 数据一致性检查

 🛠️ 技术架构

 技术栈详情

| 组件 | 技术选型 | 版本 | 用途说明 |
|------|----------|------|----------|
| 编程语言 | Python | 3.8+ | 测试脚本开发 |
| 测试框架 | Pytest | 7.4+ | 测试用例管理和执行 |
| 浏览器自动化 | Selenium | 4.15+ | Web 界面自动化操作 |
| 报告生成 | Pytest-html | 4.1+ | HTML 测试报告生成 |
| 依赖管理 | Pip | 最新版 | Python 包管理 |

 系统架构图

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   测试用例层     │    │   页面对象层      │    │   浏览器驱动层   │
│                 │    │                  │    │                 │
│ • 业务测试逻辑   │◄───│ • 页面元素封装    │◄───│ • 浏览器操作     │
│ • 数据驱动测试   │    │ • 页面操作方法    │    │ • 元素定位       │
│ • 断言验证       │    │ • 业务流组合      │    │ • 等待机制       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                         ┌─────────────────┐
                         │   配置管理层     │
                         │                 │
                         │ • 环境配置       │
                         │ • 测试数据       │
                         │ • 报告配置       │
                         └─────────────────┘
```

 📖 使用指南

 基础使用

 运行完整测试套件
```bash
 运行全面的 PIM 模块测试
python run_comprehensive_test.py

 输出示例：
 🎯 开始 OrangeHRM PIM 模块全面测试
 🔐 登录 OrangeHRM... ✅ 登录成功
 👥 测试添加员工... ✅ 员工添加成功
 🔍 测试搜索员工... ✅ 搜索功能正常
```

 运行特定测试模块
```bash
 只运行 PIM 模块测试
pytest tests/test_pim.py -v

 运行单个测试用例
pytest tests/test_pim.py::TestPIMFunctionality::test_add_employee -v
```

 高级功能

 生成详细测试报告
```bash
 生成 HTML 格式的测试报告
pytest tests/complete_pim_test.py -v --html=reports/detailed_report.html

 包含截图的完整报告
pytest tests/complete_pim_test.py -v --html=reports/full_report.html --self-contained-html
```

 参数化测试执行
```bash
 多进程并行测试
pytest tests/ -n 4

 指定浏览器类型
pytest tests/ --browser=firefox

 无界面模式运行
pytest tests/ --headless
```

 代码示例

 页面对象使用示例
```python
from src.pages.login_page import LoginPage
from src.pages.pim_page import PIMPage

 初始化页面对象
login_page = LoginPage(driver)
pim_page = PIMPage(driver)

 执行登录操作
login_page.login("Admin", "admin123")

 添加新员工
pim_page.add_employee("张", "三", "EMP001")

 验证员工添加成功
assert pim_page.is_employee_exists("张三")
```

 自定义测试用例
```python
import pytest
from src.utils.config import Config

class TestCustomScenario:
    """自定义测试场景"""
    
    @pytest.mark.parametrize("employee_data", [
        {"first_name": "李", "last_name": "四", "id": "EMP002"},
        {"first_name": "王", "last_name": "五", "id": "EMP003"}
    ])
    def test_multiple_employees(self, employee_data):
        """测试批量添加员工"""
        pim_page = PIMPage(self.driver)
        
         添加员工
        pim_page.add_employee(
            employee_data["first_name"],
            employee_data["last_name"],
            employee_data["id"]
        )
        
         验证添加成功
        assert pim_page.get_success_message() == "Successfully Saved"
```

 ⚙️ 配置说明

 配置文件详解

```python
 config.py - 完整配置示例
class Config:
    """OrangeHRM 自动化测试配置类"""
    
     ==================== 应用配置 ====================
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"
    PIM_URL = f"{BASE_URL}/web/index.php/pim/viewEmployeeList"
    
     ==================== 测试账号配置 ====================
    USERNAME = "Admin"
    PASSWORD = "admin123"
    
     ==================== 浏览器配置 ====================
    BROWSER = "chrome"   可选: chrome, firefox, edge
    HEADLESS = False     无界面模式
    WINDOW_SIZE = "1920,1080"   浏览器窗口大小
    
     ==================== 等待配置 ====================
    IMPLICIT_WAIT = 10      隐式等待时间（秒）
    EXPLICIT_WAIT = 15      显式等待时间（秒）
    POLL_FREQUENCY = 0.5    等待轮询频率（秒）
    
     ==================== 测试数据配置 ====================
    TEST_FIRST_NAME = "Test"
    TEST_LAST_NAME_PREFIX = "User"
    
     ==================== 路径配置 ====================
    REPORT_DIR = "reports"
    SCREENSHOT_DIR = "screenshots"
    LOG_DIR = "logs"
    
     ==================== 报告配置 ====================
    REPORT_TITLE = "OrangeHRM 自动化测试报告"
    REPORT_THEME = "standard"   可选: standard, dark
    
    @classmethod
    def get_unique_employee_name(cls):
        """生成唯一的员工姓名"""
        import time
        timestamp = int(time.time())
        return f"{cls.TEST_FIRST_NAME}", f"{cls.TEST_LAST_NAME_PREFIX}{timestamp}"
    
    @classmethod
    def setup_directories(cls):
        """创建必要的目录结构"""
        import os
        for directory in [cls.REPORT_DIR, cls.SCREENSHOT_DIR, cls.LOG_DIR]:
            os.makedirs(directory, exist_ok=True)
```

 环境特定配置

 开发环境配置
```python
 config_development.py
class DevelopmentConfig(Config):
    """开发环境配置"""
    HEADLESS = False
    IMPLICIT_WAIT = 5
    BASE_URL = "http://localhost:8080"
```

 生产环境配置
```python
 config_production.py  
class ProductionConfig(Config):
    """生产环境配置"""
    HEADLESS = True
    IMPLICIT_WAIT = 10
    BASE_URL = "https://your-production-orangehrm.com"
```

 🔧 故障排除

 常见问题解决方案

 1. 浏览器驱动问题
症状: WebDriver 初始化失败
```bash
 解决方案：确保 Chrome 驱动正确安装
 检查 Chrome 版本
google-chrome --version

 下载对应版本的 ChromeDriver
 或者使用 webdriver-manager 自动管理
pip install webdriver-manager
```

 2. 元素定位失败
症状: NoSuchElementException 错误
```python
 解决方案：使用更健壮的定位策略
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 使用显式等待
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)

 使用多种定位策略组合
def find_element_robust(locators):
    for locator in locators:
        try:
            return driver.find_element(locator)
        except NoSuchElementException:
            continue
    raise NoSuchElementException("所有定位策略都失败")
```

 3. 测试数据冲突
症状: 员工信息重复导致测试失败
```python
 解决方案：使用唯一标识符
import time
import random

def generate_unique_employee_data():
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)
    return {
        "first_name": f"Test{timestamp}",
        "last_name": f"User{random_suffix}",
        "employee_id": f"EMP{timestamp}{random_suffix}"
    }
```

 调试技巧

 启用详细日志
```python
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)
```

 失败时自动截图
```python
def test_with_screenshot():
    try:
         测试代码
        assert True
    except Exception as e:
         失败时截图
        driver.save_screenshot(f"failure_{int(time.time())}.png")
         记录页面源码
        with open(f"page_source_{int(time.time())}.html", "w") as f:
            f.write(driver.page_source)
        raise e
```

 🤝 贡献指南

 开发环境设置

1. Fork 项目仓库
2. 克隆到本地
   ```bash
   git clone https://github.com/your-username/orangehrm-automation.git
   cd orangehrm-automation
   ```

3. 创建特性分支
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. 提交更改
   ```bash
   git commit -m "Add amazing feature"
   ```

5. 推送到分支
   ```bash
   git push origin feature/amazing-feature
   ```

6. 创建 Pull Request

 代码规范

 Python 代码风格
```python
 遵循 PEP 8 规范
class TestExample:
    """测试类文档字符串"""
    
    def test_method(self, parameter_one, parameter_two):
        """方法文档字符串"""
         使用有意义的变量名
        expected_result = "success"
        actual_result = self.execute_test()
        
         清晰的断言消息
        assert actual_result == expected_result, \
            f"期望结果: {expected_result}, 实际结果: {actual_result}"
```

 测试代码规范
- 每个测试方法只测试一个功能点
- 使用描述性的测试方法名称
- 包含必要的注释和文档字符串
- 确保测试的独立性和可重复性

 🗺️ 开发路线图

 近期目标 (1-3 个月)
- [ ] API 测试集成
  - REST API 自动化测试
  - 数据库验证测试
  - 接口性能测试

- [ ] 持续集成流水线
  - GitHub Actions 集成
  - Jenkins 流水线配置
  - 自动化部署脚本

 中期目标 (3-6 个月)
- [ ] 多浏览器支持
  - Firefox 浏览器支持
  - Edge 浏览器支持
  - 跨浏览器兼容性测试

- [ ] 移动端测试
  - 响应式设计测试
  - 移动浏览器兼容性
  - PWA 应用测试

 长期愿景 (6-12 个月)
- [ ] AI 增强测试
  - 智能元素定位
  - 自适应测试用例生成
  - 异常模式识别

- [ ] 云测试平台
  - SaaS 化测试服务
  - 分布式测试执行
  - 实时测试监控

 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

 许可证摘要
```text
MIT License

版权所有 (c) 2024 OrangeHRM 自动化测试项目

特此免费授予任何获得本软件及相关文档文件（以下简称"软件"）副本的人士，
无限制地处理本软件的权限，包括但不限于使用、复制、修改、合并、发布、分发、再许可的权利。

本软件按"原样"提供，不附带任何明示或暗示的担保，包括但不限于对适销性、
特定用途适用性和非侵权性的担保。在任何情况下，作者或版权持有人均不对
因软件或使用或其他方式引起的任何索赔、损害或其他责任负责。
```

 🙏 致谢

 技术支持
- [OrangeHRM](https://www.orangehrm.com/) - 优秀的人力资源管理系统
- [Selenium](https://selenium.dev/) - 强大的 Web 自动化框架
- [Pytest](https://pytest.org/) - 优雅的 Python 测试框架

 贡献者
感谢所有为这个项目做出贡献的开发者们！

 社区支持
特别感谢测试自动化社区的宝贵反馈和建议。

---

<div align="center">

 💫 开始使用

立即开始您的 OrangeHRM 自动化测试之旅！

[![快速开始](https://img.shields.io/badge/快速开始-指南-blue?style=for-the-badge)](-快速开始)
[![文档](https://img.shields.io/badge/详细文档-查看-green?style=for-the-badge)](-使用指南)
[![问题反馈](https://img.shields.io/badge/问题反馈-Issues-red?style=for-the-badge)](https://github.com/your-username/orangehrm-automation/issues)

如果这个项目对您有帮助，请给个 ⭐ Star 支持一下！

</div>

 📞 联系我们

 项目维护团队
- 项目负责人: Peacher(https://github.com/your-username)
- 技术负责人: Peacher(https://github.com/tech-lead)
- 质量保证: [QA Team](mailto:qa-team@example.com)

 沟通渠道
- 📧 邮箱: 2973395744@qq.com
- 💬 讨论区: [GitHub Discussions](https://github.com/your-username/orangehrm-automation/discussions)
- 🐛 问题反馈: [GitHub Issues](https://github.com/your-username/orangehrm-automation/issues)
- 📚 文档网站: [项目 Wiki](https://github.com/your-username/orangehrm-automation/wiki)

 

<div align="center">

⭐ 如果您觉得这个项目有用，请不要忘记给我一个 Star！您的支持是我持续改进的动力。

</div>
