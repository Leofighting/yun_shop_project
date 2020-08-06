# -*- coding:utf-8 -*-
__author__ = "leo"

import os

print(os.path.dirname(os.path.dirname(os.getcwd())))
file = os.path.dirname(os.path.dirname(os.getcwd())) + "/screenshot/"
if not os.path.exists(file):
    os.mkdir(file)