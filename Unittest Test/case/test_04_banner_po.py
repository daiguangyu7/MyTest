import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminBannerPage import AdminBannerPage 
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_banner_page = AdminBannerPage(cls.driver)
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

    def test_01_reset(self):
        # 重置搜索内容
        self.admin_index_page.click_banner()

        self.admin_banner_page.reset_search()
        time.sleep(2)
        e  = self.driver.find_element_by_xpath(self.admin_banner_page.search[-1])
        assert len(e.text) == 0
    
    def test_02_search_banner(self):
        # 搜索banner
        self.admin_index_page.click_banner()

        self.admin_banner_page.search_banner('两只企鹅')
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_banner_page.b_text[-1])
        assert len(e.text) != 0
    
    def test_03_update_banner_desc(self):
        # 修改banner描述信息
        self.admin_index_page.click_banner()
        time.sleep(2)

        self.admin_banner_page.update_banner_desc("py测试1111111")
        time.sleep(2)
    
    def test_04_reset(self):
        # 重置搜索内容
        self.admin_index_page.click_banner()

        self.admin_banner_page.reset_search()
        time.sleep(2)
        e  = self.driver.find_element_by_xpath(self.admin_banner_page.search[-1])
        assert len(e.text) == 0



