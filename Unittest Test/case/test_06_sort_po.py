import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminSortPage import AdminSortPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_sort_page = AdminSortPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.admin_login_page.open_url()
        # 判断是否已经登录，如果已经登陆了，就不要再的登陆
        # 如果没有登录，就去登录
        e = self.driver.find_elements_by_xpath(self.admin_index_page.log[-1])
        if len(e) == 0:
            self.admin_login_page.login('admin', '123456')
    
    def test_01_sort(self):
        # 点击分类管理
        self.admin_index_page.click_sort()
        time.sleep(2)

        e = self.driver.find_element_by_xpath(self.admin_sort_page.sort_title[-1])
        assert e.text == "分类列表"
    
    def test_02_display_hide_sort(self):
        # 显示/隐藏分类
        self.admin_index_page.click_sort()
        self.admin_sort_page.display_hide_sort()
        time.sleep(2)

        e = self.driver.find_element_by_xpath(self.admin_sort_page.sort_status[-1])
        assert e.text in ('显示', '隐藏')

    def test_03_update_sort(self):
        # 修改分类排序
        self.admin_index_page.click_sort()

        self.admin_sort_page.update_sort(999)
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_sort_page.sort_result[-1])
        assert int(e.text) == 999

    def test_04_mass_del(self): 
        # 批量删除分类
        self.admin_index_page.click_sort()

        self.admin_sort_page.mass_del()
        time.sleep(2)
  

    