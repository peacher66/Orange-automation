#!/usr/bin/env python3
"""
OrangeHRM PIM模块自动化测试运行脚本 - 修复版
"""

import pytest
import sys
import os
from pathlib import Path


def setup_directories():
    """创建必要的目录"""
    directories = ["reports", "screenshots"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)


def main():
    """主函数"""
    # 获取项目根目录
    project_root = Path(__file__).parent
    os.chdir(project_root)

    # 创建必要的目录
    setup_directories()

    # 检查测试文件是否存在
    test_file = "tests/test_pim.py"

    if not os.path.exists(test_file):
        print(f"❌ 测试文件不存在: {test_file}")
        return 1

    print(f"🚀 开始运行测试: {test_file}")
    print(f"📁 当前工作目录: {os.getcwd()}")

    # 设置测试参数
    test_args = [
        test_file,
        "-v",  # 详细输出
        "--html=reports/pim_test_report.html",
        "--self-contained-html",
        "--tb=short",  # 简化错误跟踪
    ]

    # 添加自定义参数
    if len(sys.argv) > 1:
        test_args.extend(sys.argv[1:])

    # 运行测试
    exit_code = pytest.main(test_args)

    # 输出测试结果
    if exit_code == 0:
        print("🎉 所有测试通过!")
    else:
        print(f"❌ 测试失败，退出码: {exit_code}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())