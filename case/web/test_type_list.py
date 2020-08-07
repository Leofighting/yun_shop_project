# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from properties.settings import YUN_SHOP_INDEX, TIME_RECORD
from public.save_screenshot import SaveScreenshot


class TestTypeList(unittest.TestCase):
    """
    测试搜索功能
    """

    def setUp(self) -> None:
        """
        初始化：
        1.启动 Chrome 浏览器
        2.打开云商首页
        3.窗口最大化
        4.记录开始时间
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get(YUN_SHOP_INDEX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print("start time:{}".format(TIME_RECORD))

    def tearDown(self) -> None:
        """
        结束清理模块：
        1.记录结束时间
        2.报错截屏
        3.退出浏览器
        :return:
        """
        SaveScreenshot(self.driver).save_screenshot()
        time.sleep(2)
        self.driver.quit()

    def test_type_list01(self):
        """
        点击第1个一级分类
        :return:
        """
        element = self.driver.find_element_by_xpath("//dl[@class='type'][1]//div[@class='mbig']//a[1]")
        # 获取一级分类的文本
        type_text = element.text
        element.click()
        # 获取 您的当前位置…… 的文本
        result_text = self.driver.find_element_by_xpath("//div[@class='dh']").text
        # 断言 type_text 是否包含在 result_text
        self.assertIn(type_text, result_text)

    def test_type_list02(self):
        """
        点击中间1个二级分类
        :return:
        """
        # 一级分类
        element1 = self.driver.find_element_by_xpath("//dl[@class='type'][5]//div[@class='mbig']//a[1]")
        # 鼠标悬停
        ActionChains(self.driver).move_to_element(element1).perform()
        time.sleep(1)
        element2 = self.driver.find_element_by_xpath(
            "//dl[@class='type'][5]//div[@class='mshow']/div[@class='mbox'][5]//a"
        )
        type_text = element2.text
        element2.click()

        result_text = self.driver.find_element_by_xpath("//div[@class='dh']").text
        self.assertIn(type_text, result_text)

    def test_type_list03(self):
        """
        二级分类商品为空的页面展示
        :return:
        """
        # 一级分类
        element1 = self.driver.find_element_by_xpath("//dl[@class='type'][5]//div[@class='mbig']//a[1]")
        # 鼠标悬停
        ActionChains(self.driver).move_to_element(element1).perform()
        time.sleep(1)
        element2 = self.driver.find_element_by_xpath(
            "//dl[@class='type'][5]//div[@class='mshow']/div[@class='mbox'][3]//a"
        )
        type_text = element2.text
        element2.click()

        result_text = self.driver.find_element_by_xpath("//div[@class='dh']").text
        self.assertIn(type_text, result_text)

        null_text = self.driver.find_element_by_class_name("nomsg").text
        self.assertIn("抱歉，没有找到相关的商品", null_text)


if __name__ == '__main__':
    unittest.main()
