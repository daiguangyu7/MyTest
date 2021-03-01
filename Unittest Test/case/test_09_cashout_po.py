import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminCashoutPage import AdminCashoutPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_cashout_page = AdminCashoutPage(cls.driver)
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
    
    def test_01_cashout(self):
        # 点击提现管理
        self.admin_index_page.click_cashout()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_cashout_page.click_cashout_result[-1])
        assert e.text == "提现列表"

    def test_02_search_by_tel(self):
        # 根据用户手机号搜索
        self.admin_index_page.click_cashout()
        self.admin_cashout_page.search_by_tel("18785484592")
        e = self.driver.find_element_by_xpath(self.admin_cashout_page.search_result[-1])
        assert e.text == "18785484592"

    def test_03_cashout_verify(self):
        # 审核提现申请
        self.admin_index_page.click_cashout()

        self.admin_cashout_page.cashout_verify()
        time.sleep(2)
        e = self.driver.find_elements_by_xpath(self.admin_cashout_page.verify_result[-1])
        assert e.text == "申请通过"

    

    

    