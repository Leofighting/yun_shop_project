# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest


def create_suite(file_path):
    """创建单元测试容器"""
    test_unit = unittest.TestSuite()

    # 搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(file_path, pattern="test*.py", top_level_dir=None)

    for test_suite in discover:
        for case_name in test_suite:
            test_unit.addTest(case_name)

    return test_unit
