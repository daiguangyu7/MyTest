import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminOrderPage import AdminOrderPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_order_page = AdminOrderPage(cls.driver)
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
    
    def test_01_order(self):
        # 点击订单管理
        self.admin_index_page.click_order()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_order_page.click_order_result[-1])
        assert e.text == "商品订单列表"

    def test_02_search_order(self):
        # 根据订单编号搜索订单
        self.admin_index_page.click_order()

        self.admin_order_page.search_order("161363307726950")
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_order_page.search_result[-1])
        assert e.text == "161363307726950"

    def test_03_order_status(self):
        # 根据订单状态搜索
        self.admin_index_page.click_order()

        self.admin_order_page.order_status()
        time.sleep(2)

    def test_04_order_send(self):
        # 订单发货
        self.admin_index_page.click_order()
        time.sleep(2)
        self.admin_order_page.order_status()
        time.sleep(2)
        self.admin_order_page.order_send("21547912745", "包邮")
        time.sleep(2)

    def test_05_import_order(self):
        # 导出订单
        self.admin_index_page.click_order()
        time.sleep(2)
        self.admin_order_page.import_order()
        time.sleep(3)
