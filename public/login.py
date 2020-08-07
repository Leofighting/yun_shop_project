# -*- coding:utf-8 -*-
__author__ = "leo"

import time


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        time.sleep(1)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_class_name("login_submit").click()
