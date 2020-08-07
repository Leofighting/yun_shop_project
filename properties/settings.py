# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import os

# 记录时间
TIME_RECORD = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 文件生成时间
FILE_TIME = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))

# 年月日
DAY = time.strftime("%Y-%m-%d", time.localtime(time.time()))

# 云商城首页链接
YUN_SHOP_INDEX = "http://101.133.169.100/yuns/"
# 后台管理系统链接
ADMIN_INDEX = "http://101.133.169.100/yuns/index.php/admin/index/index"

# 项目主文件夹路径
PROJECT_FILE = os.path.dirname(os.getcwd())

# web 测试用例文件夹
WEB_CASE_PATH_ = os.getcwd() + "\\case\\web\\"
WEB_CASE_PATH = str(WEB_CASE_PATH_)

# 测试报告存放路径
REPORT_PATH = os.getcwd() + "\\report\\"
