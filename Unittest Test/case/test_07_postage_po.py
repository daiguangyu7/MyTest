import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminPostagePage import AdminPostagePage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_postage_page = AdminPostagePage(cls.driver)
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
    
    def test_01_postage(self):
        # 点击邮费管理
        self.admin_index_page.click_postage()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_postage_page.postage_title[-1])
        assert e.text == "邮费列表"

    def test_02_search_postage(self):
        # 搜索邮费
        self.admin_index_page.click_postage()

        self.admin_postage_page.search_postage("中通")
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_postage_page.search_result[-1])
        assert e.text == "中通"

    def test_03_add_postage(self):
        # 新增邮费模板
        self.admin_index_page.click_postage()

        self.admin_postage_page.add_postage("百世快递", 20)
        time.sleep(2)
        self.admin_postage_page.search_postage("百世快递")
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_postage_page.search_result[-1])
        assert e.text == "百世快递"

    def test_04_update_postage_price(self):
        # 修改邮费价格
        self.admin_index_page.click_postage()

        self.admin_postage_page.update_postage_price(20)
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_postage_page.price_result[-1])
        assert float(e.text) == 20.00

    def test_04_update_prov(self):
        # 分配省份
        self.admin_index_page.click_postage()

        self.admin_postage_page.update_prov()

    def test_05_del_postage(self):
        # 删除邮费模板
        self.admin_index_page.click_postage()

        self.admin_postage_page.del_postage()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_postage_page.del_result[-1])
        assert e.text != "江浙沪包邮"
    
    
   