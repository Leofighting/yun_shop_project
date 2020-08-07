# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from properties.settings import YUN_SHOP_INDEX, TIME_RECORD
from public.save_screenshot import SaveScreenshot


class TestSearch(unittest.TestCase):
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

    def test_search01(self):
        """
        搜索框输入-内容为空
        :return:
        """
        input_element = self.driver.find_element_by_class_name("but1")
        input_element.send_keys("")
        search_button = self.driver.find_element_by_class_name("but2")
        search_button.click()

        # 统计第一页搜索结果个数
        search_count = len(self.driver.find_elements_by_class_name("gbox"))
        # 断言 search_count 是否等于8
        self.assertEqual(search_count, 8)

    def test_search02(self):
        """
        搜索框输入-内容为JavaScript脚本
        :return:
        """
        input_element = self.driver.find_element_by_class_name("but1")
        input_element.send_keys("alert('hello')")
        search_button = self.driver.find_element_by_class_name("but2")
        search_button.click()

        # 获取页面显示文本
        return_text = self.driver.find_element_by_xpath("//div").text

        # 断言 "不合法参数" 是否包含在 return_text 中
        self.assertIn("不合法参数", return_text)

    def test_search03(self):
        """
        搜索框输入-通过复制粘贴输入内容
        :return:
        """
        input_element = self.driver.find_element_by_class_name("but1")
        input_element.send_keys("男装")
        input_element.send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        input_element.send_keys(Keys.CONTROL, "x")
        time.sleep(1)
        input_element.send_keys(Keys.CONTROL, "v")
        time.sleep(1)
        search_button = self.driver.find_element_by_class_name("but2")
        search_button.click()
        result_elements = self.driver.find_elements_by_xpath("//div[@class='nm']/a")

        for element in result_elements:
            self.assertIn("男装", element.text)

    def test_search04(self):
        """
        无搜索结果页面
        :return:
        """
        input_element = self.driver.find_element_by_class_name("but1")
        input_element.send_keys("蔬菜")
        search_button = self.driver.find_element_by_class_name("but2")
        # 点击回车键
        search_button.send_keys(Keys.ENTER)
        # 获取无结果信息提示文本
        result_text = self.driver.find_element_by_class_name("nomsg").text

        # 断言文本内容
        self.assertEqual("抱歉，没有找到相关的商品", result_text)

    def test_search05(self):
        """
        模糊匹配-匹配商品标题开头
        :return:
        """
        input_element = self.driver.find_element_by_class_name("but1")
        input_element.send_keys("BOY")
        search_button = self.driver.find_element_by_class_name("but2")
        # 点击回车键
        search_button.send_keys(Keys.ENTER)
        result_elements = self.driver.find_elements_by_xpath("//div[@class='nm']/a")

        for element in result_elements:
            result = element.text.startswith("BOY")
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
