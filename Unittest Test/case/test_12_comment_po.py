import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminCommentPage import AdminCommentPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_comment_page = AdminCommentPage(cls.driver)
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
    
    def test_01_click_comment(self):
        # 点击评论管理
        self.admin_index_page.click_comment()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_index_page.comment_result[-1])
        assert e.text == "评论列表"

    def test_02_search_comment(self):
        # 搜索评论内容
        self.admin_index_page.click_comment()
        self.admin_comment_page.search_comment("11111")
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_comment_page.search_comment_result[-1])
        assert e.text == "11111"

    def test_03_dis_hid_comment(self):
        # 展示/隐藏评论
        self.admin_index_page.click_comment()
        time.sleep(2)
        self.admin_comment_page.dis_hid_comment()
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_comment_page.dis_hi_result[-1])
        assert e.text in ('展示', '未展示')

    def test_04_top_comment(self):
        # 置顶评论
        self.admin_index_page.click_comment()
        time.sleep(2)
        self.admin_comment_page.top_comment()


    