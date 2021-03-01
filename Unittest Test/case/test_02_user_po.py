import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminUserPage import AdminUserPage

class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_user_page = AdminUserPage(cls.driver)
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
    
    def test_01_search_user(self):
        # 搜索用户
        self.admin_index_page.click_user()
        self.admin_user_page.search('爱我请给我打钱')
        time.sleep(3)
    
    def test_02_freeze_unfreeze_user(self):
        # 冻结或解冻用户
        self.admin_index_page.click_user()
        self.admin_user_page.search('爱我请给我打钱')

        self.admin_user_page.freeze_unfreeze()
        time.sleep(3)
        e = self.driver.find_element_by_xpath(self.admin_user_page.f_result[-1])
        assert e.text in ('正常', '禁用')
    
    def test_03_page_to(self):
        # 前往某一页
        self.admin_index_page.click_user()
        self.admin_user_page.page()
        time.sleep(3)
    
    def test_04_user_info(self):
        # 查看用户信息
        self.admin_index_page.click_user()
        self.admin_user_page.user_info()

