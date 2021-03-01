import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminGoodPage import AdminGoodPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_good_page = AdminGoodPage(cls.driver)
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
    
    def test_01_on_off_goods(self):
        # 上架/下架商品
        self.admin_index_page.click_goods()

        self.admin_good_page.on_sale()
        time.sleep(3)
        e = self.driver.find_element_by_xpath(self.admin_good_page.on_result[-1])
        assert e.text in ('上架', '下架')
    
    def test_02_start_stop_pic(self):
        # 启用/禁用商品图片
        self.admin_index_page.click_goods()
        time.sleep(2)
        self.admin_good_page.start_stop_pic()
        e = self.driver.find_element_by_xpath(self.admin_good_page.p_result[-1])
        assert e.text in ('有效', '无效')
    
    def test_03_update_good_sort(self):
        # 修改商品分类
        self.admin_index_page.click_goods()
        time.sleep(2)
        self.admin_good_page.update_good_sort()
        time.sleep(2)
    
    def test_04_search_name(self):
        # 搜索商品名称
        self.admin_index_page.click_goods()

        self.admin_good_page.search_name('星空')
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_good_page.s_result[-1])
        assert len(e.text) != 0

    def test_05_update_price(self):
        # 修改商品价格
        self.admin_index_page.click_goods()
        self.admin_good_page.search_name('星空')
        time.sleep(2)
        self.admin_good_page.update_specs(2)
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_good_page.u_result[-1])
        assert int(e.text) == 2

    def test_06_del_good(self):
        # 删除商品
        self.admin_index_page.click_goods()
        time.sleep(2)
        self.admin_good_page.del_good()
        time.sleep(2)
    