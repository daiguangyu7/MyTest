import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminSysPage import AdminSysPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_sys_page = AdminSysPage(cls.driver)
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
    
    def test_01_click_sys(self):
        # 点击系统管理
        self.admin_index_page.click_sys()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_index_page.sys_bt_result[-1])
        assert e.text == "系统配置"

    def test_02_update_sys(self):
        # 修改销售额
        self.admin_index_page.click_sys()

        self.admin_sys_page.update_sys(300)