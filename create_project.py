# 创建完整的项目结构脚本 create_project.py
import os
from pathlib import Path


def create_project_structure():
    """创建完整的项目结构"""

    # 创建目录
    directories = [
        "src/pages",
        "src/utils",
        "tests",
        "reports",
        "screenshots"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # 创建 __init__.py 文件
        init_file = Path(directory) / "__init__.py"
        init_file.touch()

    print("✅ 项目结构创建完成!")

    # 创建基础文件
    create_basic_files()


def create_basic_files():
    """创建基础文件"""

    # requirements.txt
    requirements = """selenium>=4.15.0
pytest>=7.4.0
pytest-html>=4.1.0
webdriver-manager>=4.0.1
"""

    with open("requirements.txt", "w") as f:
        f.write(requirements)

    print("✅ 基础文件创建完成!")


if __name__ == "__main__":
    create_project_structure()