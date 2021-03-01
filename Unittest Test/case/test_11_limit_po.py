import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminLimitPage import AdminLimitPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_limit_page = AdminLimitPage(cls.driver)
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
    
    def test_01_admin_limit(self):
        # 点击管理员权限管理
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_limit()
        time.sleep(2)
    
    def test_02_add_admin(self):
        # 添加管理员
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_limit()
        time.sleep(2)
        self.admin_limit_page.add_admin("aaa1", "aaa1", 'aaa1')
    
    def test_03_reset_pass(self):
        # 重置密码
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_limit()
        time.sleep(2)

    def test_04_click_admin_role(self):
        # 点击角色管理
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_role()

    def test_05_add_role(self):
        # 新增角色
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_role()
        time.sleep(2)
        self.admin_limit_page.add_role("test12")

    def test_06_set_limit(self):
        # 设置权限
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_role()

        self.admin_limit_page.set_limit()

    def test_07_update_role(self):
        # 修改角色名
        self.admin_index_page.click_limit()
        time.sleep(2)
        self.admin_limit_page.click_admin_role()
        time.sleep(2)
        self.admin_limit_page.update_role('test1122')
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_limit_page.update_role_result[-1])
        assert e.text == 'test1122'




    