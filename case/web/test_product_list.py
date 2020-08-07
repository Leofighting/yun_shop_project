# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import unittest

from selenium import webdriver

from properties.settings import YUN_SHOP_INDEX, TIME_RECORD, ADMIN_INDEX
from public.login import Login
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
        self.driver.get(ADMIN_INDEX)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        Login(self.driver).login()
        print("start time:{}".format(TIME_RECORD))
        time.sleep(1)

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

    def test_product_list01(self):
        """
        商品列表页面
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“商品列表”
        product_list_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[1]")
        # 获取商品列表元素的 class 属性值
        product_list_class = product_list_element.get_attribute("class")
        self.assertEqual(product_list_class, "lname ch")

    def test_product_list02(self):
        """
        添加产品功能
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加产品”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 获取 选择分类 文本
        check_text = self.driver.find_element_by_xpath("//div[@class='cnav']/a").text
        # 发布宝贝 按钮不可用
        button_status = self.driver.find_element_by_id("submit_cats").is_enabled()
        # 断言
        self.assertEqual("选择分类", check_text)
        self.assertFalse(button_status)

    def test_product_list03(self):
        """
        选择分类-各级分类均选择中间1项，发布宝贝
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加产品”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        time.sleep(1)
        # 选择中间的一级分类
        type_1_element = self.driver.find_element_by_xpath("//a[@data-cid='8']")
        type_1_element.click()
        # 获取一级分类文本
        type_1_text = type_1_element.text
        # 选择中间的二级分类
        type_2_element = self.driver.find_element_by_xpath("//a[@data-cid='108']")
        type_2_element.click()
        # 获取二级分类文本
        type_2_text = type_2_element.text
        # 点击 “发布宝贝”
        self.driver.find_element_by_id("submit_cats").click()
        # 获取 编辑产品 文本
        check_text = self.driver.find_element_by_class_name("back").text
        # 获取 产品分类 文本
        check_text1 = self.driver.find_element_by_class_name("cts").text
        # 断言
        self.assertEqual("编辑产品", check_text)
        self.assertIn(type_1_text, check_text1)
        self.assertIn(type_2_text, check_text1)

    def test_product_list04(self):
        """
        删除确认弹窗-取消
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位删除按钮
        delete_button = self.driver.find_element_by_xpath("//a[@data-id='188']")
        delete_button.click()
        self.driver.switch_to.alert.dismiss()
        try:
            delete_button.is_displayed()
            result = True
        except:
            result = False
        self.assertTrue(result)

    def test_product_list05(self):
        """
        删除确认弹窗-确定
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        time.sleep(1)
        # 切换 iframe
        self.driver.switch_to.frame("content")
        time.sleep(1)
        # 定位删除按钮
        delete_button = self.driver.find_element_by_xpath("//a[@data-id='85']")
        delete_button.click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        delete_buttons = self.driver.find_elements_by_class_name("del")
        result = ""
        # 循环判断：data-id 的值是否存在 已经删除的 “85”
        for element in delete_buttons:
            if "85" in element.get_attribute("data-id"):
                result = False
            else:
                result = True
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()