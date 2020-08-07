# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import sys

from properties.settings import DAY
from public.create_suite import create_suite
from public.save_report import SaveReport

# 获取主项目路径，文件名
dir_name, file_name = os.path.split(os.path.abspath(sys.argv[0]))
# web 测试用例路径
case_path = ".\\case\\web\\"
# 测试报告存放总路径
report_file = dir_name + "\\report\\"
# 测试用例集
test_cases = create_suite(case_path)
# 测试报告存放文件夹，按日期命名
report_path = report_file + DAY
# 执行测试用例并生成测试报告
SaveReport(report_path).create_report(test_cases)
