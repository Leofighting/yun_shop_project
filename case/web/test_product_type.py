# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from properties.settings import TIME_RECORD, ADMIN_INDEX
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

    def test_product_type01(self):
        """
        产品分类页面
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 获取商品列表元素的 class 属性值
        product_list_class = product_type_element.get_attribute("class")
        self.assertEqual(product_list_class, "lname ch")

    def test_product_type02(self):
        """
        父级分类-不选择任何父级分类
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        time.sleep(1)
        # 获取 添加分类 文本
        check_text = self.driver.find_element_by_class_name("back").text
        # 断言
        self.assertEqual("添加分类", check_text)

    def test_product_type03(self):
        """
        添加分类页面
        :return:
        """
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 输入分类名称
        self.driver.find_element_by_id("name").send_keys("男上衣")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value='1']").click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value='1']").click()
        # 点击保存按钮
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        check_text = self.driver.find_element_by_xpath("//tbody/tr[last()]/td[2]").text
        self.assertEqual("男上衣", check_text)

    def test_product_type04(self):
        """
        父级分类-选择第一项
        :return:
        """
        # 分类id
        type_id = "1"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        # 输入分类名称
        self.driver.find_element_by_id("name").send_keys("男上衣")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value={}]".format(type_id)).click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value='1']").click()
        # 点击保存按钮
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        # 点击进入 data-id=type_id 一级分类的下一级
        self.driver.find_element_by_xpath("//a[@data-id='1']/following-sibling::a[2]").click()
        time.sleep(3)
        check_text = self.driver.find_element_by_xpath("//tbody/tr[last()]/td[2]").text
        self.assertEqual("男上衣", check_text)

    def test_product_type05(self):
        """
        父级分类-选择中间一项
        :return:
        """
        # 分类id
        type_id = "270"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        # 输入分类名称
        self.driver.find_element_by_id("name").send_keys("男上衣")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value='1']").click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value={}]".format(type_id)).click()
        # 点击保存按钮
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        # 点击进入 data-id=type_id 一级分类的下一级
        self.driver.find_element_by_xpath("//a[@data-id='1']/following-sibling::a[2]").click()
        time.sleep(3)
        check_text = self.driver.find_element_by_xpath("//tbody/tr[last()]/td[2]").text
        self.assertEqual("男上衣", check_text)

    def test_product_type06(self):
        """
        父级分类-选择最后一项
        :return:
        """
        # 分类id
        type_id = "281"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        # 输入分类名称
        self.driver.find_element_by_id("name").send_keys("男上衣")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value='1']").click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value={}]".format(type_id)).click()
        # 点击保存按钮
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        # 点击进入 data-id=type_id 一级分类的下一级
        self.driver.find_element_by_xpath("//a[@data-id='1']/following-sibling::a[2]").click()
        time.sleep(3)
        check_text = self.driver.find_element_by_xpath("//tbody/tr[last()]/td[2]").text
        self.assertEqual("男上衣", check_text)

    def test_product_type07(self):
        """
        名称为空值
        :return:
        """
        # 分类id
        type_id = "1"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        # 点击保存按钮
        submit_button = self.driver.find_element_by_class_name("submit")
        submit_button.click()
        time.sleep(3)
        # 保存按钮是否可见
        try:
            submit_button.is_displayed()
            result = True
        except:
            result = False
        # 断言
        self.assertTrue(result)

    def test_product_type08(self):
        """
        添加分类-名称的字符长度等于10
        :return:
        """
        # 分类id
        type_id = "1"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        # 输入分类名称
        self.driver.find_element_by_id("name").send_keys("男上衣12as！@a")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value={}]".format(type_id)).click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value='1']").click()
        # 点击保存按钮
        self.driver.find_element_by_class_name("submit").click()
        time.sleep(3)
        # 点击进入 data-id=type_id 一级分类的下一级
        self.driver.find_element_by_xpath("//a[@data-id='1']/following-sibling::a[2]").click()
        time.sleep(3)
        check_text = self.driver.find_element_by_xpath("//tbody/tr[last()]/td[2]").text
        self.assertEqual("男上衣12as！@a", check_text)

    def test_product_type09(self):
        """
        添加分类-名称的字符长度等于11
        :return:
        """
        # 分类id
        type_id = "1"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        # 定位“添加分类”按钮
        add_button = self.driver.find_element_by_class_name("add")
        add_button.click()
        # 父级分类选择第一项
        type_select = Select(self.driver.find_element_by_xpath("//select[1]"))
        type_select.select_by_value(type_id)
        self.driver.find_element_by_id("name").send_keys("男上衣12as！@a1")
        # 输入关键字
        self.driver.find_element_by_id("keywords").send_keys("T恤、衬衫等")
        # 输入描述
        self.driver.find_element_by_id("describe").send_keys("测试")
        # 首页选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_index' and @ value={}]".format(type_id)).click()
        # 推荐选择“是”
        self.driver.find_element_by_xpath("//input[@name='px_recommend' and @ value='1']").click()
        # 状态选择“开”
        self.driver.find_element_by_xpath("//input[@name='status' and @ value='1']").click()
        # 点击保存按钮
        submit_button = self.driver.find_element_by_class_name("submit")
        submit_button.click()
        time.sleep(5)
        # 保存按钮是否可见
        try:
            submit_button.is_displayed()
            result = True
        except:
            result = False

        # 断言
        self.assertTrue(result)

    def test_product_type10(self):
        """
        添加分类-下一级页面为空
        :return:
        """
        # 分类id
        type_id = "1"
        # 定位顶部菜单栏“商品”
        product_element = self.driver.find_element_by_xpath("//a[@parent-id='3']")
        product_element.click()
        # 定位左侧栏“产品分类”
        product_type_element = self.driver.find_element_by_xpath("//div[@id='top_left_3']//a[2]")
        product_type_element.click()
        # 切换 iframe
        self.driver.switch_to.frame("content")
        self.driver.find_element_by_xpath("//a[@data-id='285']/following-sibling::a[2]").click()
        # 获取校验文本
        check_text = self.driver.find_element_by_xpath("//td[@colspan='8']").text

        self.assertEqual("还没有数据，赶快添加吧！", check_text)


if __name__ == '__main__':
    unittest.main()
