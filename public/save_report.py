# -*- coding:utf-8 -*-
__author__ = "leo"

import os

from properties.settings import FILE_TIME
from report import HTMLTestRunner


class SaveReport:
    """保存测试报告"""

    def __init__(self, file):
        self.file = file

    def check_file_exist(self):
        """
        检查文件是否存在
        :return:
        """
        if not os.path.exists(self.file):
            os.mkdir(self.file)
        return True

    def create_report_file(self):
        """
        定义测试报告文件名
        :return:
        """
        report_file = self.file + "\\" + FILE_TIME + "_result.html"
        return report_file

    def create_report(self, test_case):
        """生成测试报告"""
        if self.check_file_exist():
            report_name = self.create_report_file()
            with open(report_name, "wb") as file:
                runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                                       title="云商城-测试报告",
                                                       description="执行情况：")
                runner.run(test_case)
