# -*- coding:utf-8 -*-
__author__ = "leo"

import os

from properties.settings import PROJECT_FILE, TIME_RECORD, FILE_TIME


class SaveScreenshot:
    def __init__(self, driver):
        self.driver = driver

    def save_screenshot(self):
        screenshot_file = PROJECT_FILE + "/screenshot/"
        if not os.path.exists(screenshot_file):
            os.mkdir(screenshot_file)
        print("end time:{}".format(TIME_RECORD))
        screenshot_name = screenshot_file + FILE_TIME + ".png"
        self.driver.get_screenshot_as_file(screenshot_name)
