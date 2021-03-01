import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage

class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.admin_login_page.open_url()
    def tearDown(self):
        # 判断是否在首页，如果在首页，就去点退出
        e = self.driver.find_elements_by_xpath(self.admin_index_page.log[-1])
        if len(e) != 0:
            self.driver.find_element_by_xpath(self.admin_index_page.user_menu[-1]).click()
            time.sleep(3)
            e1 = self.driver.find_element_by_xpath('//*[contains(@id, "dropdown-menu-")]') 
            e1.find_element_by_xpath('//*[text()="退出登录"]').click()
            time.sleep(3)
    
    def test_01_login(self):
        # 登录成功
        self.admin_login_page.login('admin', '123456')

        self.driver.implicitly_wait(3)
        e = self.driver.find_element_by_xpath(self.admin_index_page.log[-1])
        assert e.text == self.admin_index_page.ht_text
    
    def test_02_login_fail(self):
        # 登录失败
        self.admin_login_page.login('admin', '1234567')
    
   
    
    